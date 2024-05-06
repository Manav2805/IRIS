import queue
import sys
import time
import tkinter
import psutil as ps
import platform
import subprocess
import wmi
import threading
from bs4 import BeautifulSoup
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pylab as plt
def getBatteryReport():
    subprocess.run(['powercfg', '/batteryreport', '/output', 'battery_report.html'], capture_output=True)
    Battery_Info = {}
    with open('battery_report.html', 'r') as file:
        battery_report = file.read()
        soup = BeautifulSoup(battery_report,"lxml")
        reference_para = soup.find("span", class_ = "label")
        if (reference_para!= None):
            Installed_Batteries_Table = reference_para.find_parent("table")
            if Installed_Batteries_Table!= None:
                row = Installed_Batteries_Table.find_all("tr")
                for i in row[1:]:
                    data = i.find_all("td")
                    pair = [tr.text.strip() for tr in data]
                    if len(pair) == 2:
                        Battery_Info[pair[0]] = pair[1]
    return Battery_Info

def getBatteryCapacity():
    subprocess.run(['powercfg', '/batteryreport', '/output', 'battery_report.html'], capture_output=True)
    Battery_Capacity = []
    with open('battery_report.html', 'r') as file:
        battery_report = file.read()
        soup = BeautifulSoup(battery_report,"lxml")
        reference_para = soup.find_all("col", class_ = "col2")[-3]
        if reference_para!= None:
            Battery_Capacity_Table = reference_para.find_parent("table")
            if Battery_Capacity_Table!= None:
                row = Battery_Capacity_Table.find_all("tr")
                for i in row[1:]:
                    data = i.find_all("td")
                    pair = [tr.text.strip() for tr in data]
                    if len(pair) == 3:
                        try:
                            Battery_Capacity.append(int(pair[1].split(" ")[0].replace(",","")))
                        except ValueError:
                            Battery_Capacity.append(int(pair[1].split(" ")[0].replace(".","")))
    return Battery_Capacity


def setInfoData(canvas):
    computer = wmi.WMI()
    system_info = computer.Win32_ComputerSystem()[0]
    System_Data = system_info.Manufacturer+" " + system_info.Model
    mySys = platform.uname()
    Node_Data = mySys.node
    Release_Data = mySys.release
    Version_Data = mySys.version
    Machine_Data= mySys.machine
    Processor_Data = mySys.processor
    canvas.create_text(
        140.0,
        160.0,
        anchor="nw",
        text=System_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    )
    canvas.create_text(
        140.0,
        212.0,
        anchor="nw",
        text=Node_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    ) 
    canvas.create_text(
        140.0,
        264.0,
        anchor="nw",
        text=Release_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    ) 
    canvas.create_text(
        140.0,
        316.0,
        anchor="nw",
        text=Version_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    ) 
    canvas.create_text(
        140.0,
        368.0,
        anchor="nw",
        text=Machine_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    )
    canvas.create_text(
        140.0,
        420.0,
        anchor="nw",
        text=Processor_Data,
        fill="#7C0000",
        font=("Inter", 20 * -1),
        width = 300
    )

running = True
button = None
def releaseBreak():
    global running
    running = True

def setBreak():
    global running
    running = False

def HomeClick():
    global button
    button = "H"

def AnalyzeClick():
    global button
    button = "A"

def updateInfoGraph(l,Home_Button,Analyze_Button,response_queue):
    try:
        while running:
            initial_io = ps.disk_io_counters()
            initial_read = initial_io.read_time/initial_io.read_count
            initial_write = initial_io.write_time/initial_io.write_count
            updated_io = ps.disk_io_counters()
            updated_read = updated_io.read_time/updated_io.read_count
            updated_write = updated_io.write_time/updated_io.write_count
            average_read = (updated_read+initial_read)/2
            average_write = (updated_write+initial_write)/2
            average_time = ( average_read + average_write )/2
            l.pop(0)
            l.append(average_time*1000)
            dict = {
                "info" : l
            }
            data = pd.DataFrame(dict)
            fig = plt.Figure(figsize=(5,2.3), dpi=100)
            fig_plot = fig.add_subplot()
            fig_plot.fill_between(x = [i for i in range(1,11)], y1 = data["info"])
            fig_plot.set_yticks([0.4,0.8,1.2,1.6,2])
            response_queue.put(fig)
            time.sleep(1.5)
    except tkinter.TclError:
            pass
    releaseBreak()
    sys.exit()

def setInfoGraph(canvas,window,Home_Button,Analyze_Button):
    Home_Button.config(command = lambda: [setBreak(),HomeClick()])
    Analyze_Button.config(command = lambda: [setBreak(),AnalyzeClick()])
    l = [0]*10
    response_queue = queue.Queue()
    if running:
        io_thread = threading.Thread(target=updateInfoGraph, args=(l,Home_Button,Analyze_Button,response_queue))
        io_thread.start()
    while running:
        window.update()
        try:
            fig = response_queue.get_nowait()
            canvas = FigureCanvasTkAgg(figure=fig,master=window)
            canvas.draw()
            canvas.get_tk_widget().place(x=450,y=200)
        except queue.Empty:
            continue
        except tkinter.TclError:
            pass
    return button


Analysis_Report = getBatteryReport()
Battery_Report = getBatteryCapacity()
def setAnalyzeInfo(canvas,window):
    canvas.create_text(
        180.0,
        189.0,
        anchor="nw",
        text=Analysis_Report.get("NAME"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        243.0,
        anchor="nw",
        text=Analysis_Report.get("MANUFACTURER"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        297.0,
        anchor="nw",
        text=Analysis_Report.get("SERIAL NUMBER"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        351.0,
        anchor="nw",
        text=Analysis_Report.get("CHEMISTRY"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        405.0,
        anchor="nw",
        text=Analysis_Report.get("DESIGN CAPACITY"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        459.0,
        anchor="nw",
        text=Analysis_Report.get("FULL CHARGE CAPACITY"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        180.0,
        513.0,
        anchor="nw",
        text=Analysis_Report.get("CYCLE COUNT"),
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    fig = plt.Figure(figsize=(6,3), dpi=100)
    fig_plot = fig.add_subplot()
    dict = {
        "info" : Battery_Report
    }
    data = pd.DataFrame(dict)
    fig_plot.fill_between(x = [i for i in range(1,len(Battery_Report)+1)], y1 = data["info"])
    fig_plot.set_yticks([15000,30000,45000,60000,75000])
    fig_plot.get_xaxis().set_visible(False)
    fig_plot.set_ylabel("Capacity (mAH)")
    canvas = FigureCanvasTkAgg(figure=fig,master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=390,y=200)

Cont = True
Clicked = None
def setHomeInfo(canvas,window,Info_Button,Analyze_Button):
    Memory = ps.virtual_memory()
    In_Use = Memory.used/(1024**3)
    Available = Memory.available/(1024**3)
    Percent = Memory.percent
    CPU_Count = ps.cpu_count()
    CPU_Speed = ps.cpu_freq().current
    CPU_Interupts = ps.cpu_stats().interrupts
    canvas.create_text(
        500.0,
        399.0,
        anchor="nw",
        text=CPU_Count,
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        500.0,
        468.0,
        anchor="nw",
        text=str(CPU_Speed) + " MHz",
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        500.0,
        534.0,
        anchor="nw",
        text= CPU_Interupts,
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )
    canvas.create_text(
        160.0,
        399.0,
        anchor="nw",
        text= str(round(In_Use,2)) + " GB",
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        160.0,
        468.0,
        anchor="nw",
        text= str(round(Available,2)) + " GB",
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        160.0,
        534.0,
        anchor="nw",
        text=str(Percent) + " %",
        fill="#7C0000",
        font=("Inter", 20 * -1)
    )

def releaseCont():
    global Cont
    Cont = True

def stopCont():
    global Cont
    Cont = False

def InfoClick_Home():
    global Clicked
    Clicked = "I"

def AnalyzeClick_Home():
    global Clicked
    Clicked = "A"

def updateHomeGraph(graph_queue_mem,graph_queue_cpu,graph_queue_send,graph_queue_receive):
    Memory_data = [0]*5
    CPU_data = [0]*5
    Send_data = [0]*5
    Receive_data = [0]*5
    try:
        while Cont:
            Memory_data.pop(0)
            Memory_data.append(round(ps.virtual_memory().used/(1024**3),2))
            CPU_data.pop(0)
            CPU_data.append(ps.cpu_freq().current)
            Send_data.pop(0)
            Send_data.append(ps.net_io_counters().bytes_sent/(1024)**3)
            Receive_data.pop(0)
            Receive_data.append(ps.net_io_counters().bytes_recv/(1024)**3)

            dict = {
                "Memory" : Memory_data,
                "CPU" : CPU_data,
                "Send" : Send_data,
                "Receive" : Receive_data
            }
            data = pd.DataFrame(dict)
            mem = plt.Figure(figsize=(2.7,2), dpi=100)
            cpu = plt.Figure(figsize=(2.8,2), dpi=100)
            send = plt.Figure(figsize=(2.8,1.7), dpi=100)
            receive = plt.Figure(figsize=(2.8,1.7), dpi=100)
            fig_plot_mem = mem.add_subplot()
            fig_plot_mem.fill_between(x = [i for i in range(1,6)], y1 = data["Memory"])
            fig_plot_mem.set_yticks([6,12,18,24,30])
            fig_plot_cpu = cpu.add_subplot()
            fig_plot_cpu.fill_between(x = [i for i in range(1,6)], y1 = data["CPU"])
            fig_plot_cpu.set_yticks([1500,3000,4500,6000,7500])
            fig_plot_send = send.add_subplot()
            fig_plot_send.fill_between(x = [i for i in range(1,6)], y1 = data["Send"])
            fig_plot_send.set_yticks([1,2,3,4,5])
            fig_plot_recieve = receive.add_subplot()
            fig_plot_recieve.fill_between(x = [i for i in range(1,6)], y1 = data["Receive"])
            fig_plot_recieve.set_yticks([20,40,60,80,100])
            graph_queue_send.put(send)
            graph_queue_receive.put(receive)
            graph_queue_mem.put(mem)
            graph_queue_cpu.put(cpu)
            time.sleep(1.5)
    except tkinter.TclError:
        pass
    releaseCont()
    sys.exit()

def setHomeGraph(canvas,window,Info_Button,Analyze_Button):
    global Clicked
    Clicked = None
    Info_Button.config(command = lambda: [stopCont(),InfoClick_Home()])
    Analyze_Button.config(command = lambda: [stopCont(),AnalyzeClick_Home()])
    graph_queue_send = queue.Queue()
    graph_queue_receive = queue.Queue()
    graph_queue_mem = queue.Queue()
    graph_queue_cpu = queue.Queue()
    if Cont:
        io_thread_home = threading.Thread(target=updateHomeGraph, args=(graph_queue_mem,graph_queue_cpu,graph_queue_send,graph_queue_receive))
        io_thread_home.start()
    while Cont:
        window.update()
        try:
            fig = graph_queue_mem.get_nowait()
            canvas = FigureCanvasTkAgg(figure=fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().place(x=60, y=150)
        except queue.Empty:
            pass
        except tkinter.TclError:
            pass
        try:
            fig = graph_queue_cpu.get_nowait()
            canvas = FigureCanvasTkAgg(figure=fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().place(x=390, y=150)
        except queue.Empty:
             pass
        except tkinter.TclError:
            pass
        try:
            fig = graph_queue_send.get_nowait()
            canvas = FigureCanvasTkAgg(figure=fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().place(x=730, y=140)
        except queue.Empty:
            pass
        except tkinter.TclError:
            pass
        try:
            fig = graph_queue_receive.get_nowait()
            canvas = FigureCanvasTkAgg(figure=fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().place(x=730, y=360)
        except queue.Empty:
            pass
        except tkinter.TclError:
            pass
    if Clicked != None:
        return Clicked