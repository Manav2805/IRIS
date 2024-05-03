import time
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
                        Battery_Capacity.append(int(pair[1].split(" ")[0].replace(",","")))
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

def updateGraph(l,window,canvas,Home_Button,Analyze_Button):
    Home_Button.config(command = lambda: [setBreak(),HomeClick()])
    Analyze_Button.config(command = lambda: [setBreak(),AnalyzeClick()])
    while running:
        try:
            if window.winfo_exists():
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
                canvas = FigureCanvasTkAgg(figure=fig,master=window)
                canvas.draw()
                canvas.get_tk_widget().place(x=450,y=200)
                time.sleep(2.5)
            else:
                break
        except:
            break
    releaseBreak()
    return

def setInfoGraph(canvas,window,Home_Button,Analyze_Button):
    L = []
    for i in range(10):
        L.append(0)
    io_thread = threading.Thread(target=updateGraph, args=(L,window,canvas,Home_Button,Analyze_Button))
    io_thread.start()
    while running:
        window.update()
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
