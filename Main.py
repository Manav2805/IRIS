import os
import time
from tkinter import Tk, Canvas, Button, PhotoImage, font

from Information import setAnalyzeInfo, setInfoData, setInfoGraph

def setHome(canvas, window):
    canvas = Canvas(
    window,
    bg = "#6489B4",
    height = 582,
    width = 1041,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        56.0,
        1041.0,
        113.0,
        fill="#035C68",
        outline="")

    canvas.create_text(
        135.0,
        70.0,
        anchor="nw",
        text="Memory",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        488.0,
        70.0,
        anchor="nw",
        text="CPU",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        832.0,
        70.0,
        anchor="nw",
        text="Wi-Fi",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_rectangle(
        726.0,
        131.0,
        1020.0,
        316.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        404.0,
        399.0,
        anchor="nw",
        text="Usage",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        404.0,
        468.0,
        anchor="nw",
        text="Speed",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        404.0,
        534.0,
        anchor="nw",
        text="Processes",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        399.0,
        anchor="nw",
        text="In-Use",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        468.0,
        anchor="nw",
        text="Available",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        534.0,
        anchor="nw",
        text="Percent",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        387.0,
        131.0,
        681.0,
        370.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        48.0,
        131.0,
        342.0,
        370.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        726.0,
        320.0,
        anchor="nw",
        text="Send",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        726.0,
        543.0,
        anchor="nw",
        text="Recieve",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        726.0,
        352.0,
        1020.0,
        537.0,
        fill="#D9D9D9",
        outline="")

    Home_Button = Button(
        bg = "#6489B4",
        text = "Home",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    Home_Button.place(
        x=18.0,
        y=0.0,
        width=117.0,
        height=56.0
    )

    Info_Button = Button(
        bg = "#6489B4",
        text = "Info",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setInfo(canvas,window),
        relief="flat"
    )
    Info_Button.place(
        x=320.0,
        y=0.0,
        width=76.0,
        height=56.0
    )

    Analyze_Button = Button(
        bg = "#6489B4",
        text = "Analyze",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setAnalyze(canvas,window),
        relief="flat"
    )
    Analyze_Button.place(
        x=150.0,
        y=0.0,
        width=155.0,
        height=56.0
    )

def setInfo(canvas,window):
    canvas = Canvas(
    window,
    bg = "#6489B4",
    height = 582,
    width = 1041,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

    canvas.create_text(
        10.0,
        480.0,
        anchor="nw",
        text="IRIS is a system analysis software that I made during the summer. The primary aim is to give general system information along with the option to portray the battery report in a condensed form. This would help users check on their battery health and other information without the need to visit the multiple obscure documents and tutorial videos.\n\nThis is version 1.0",
        fill="#FFFFFF",
        font=("Inter", 15 * -1),
        width = 1050
    )
    canvas.create_rectangle(
        0.0,
        56.0,
        1041.0,
        113.0,
        fill="#035C68",
        outline="")

    canvas.create_text(
        21.0,
        58.0,
        anchor="nw",
        text="System Information",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        21.0,
        160.0,
        anchor="nw",
        text="System",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        420.0,
        anchor="nw",
        text="Processor",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        368.0,
        anchor="nw",
        text="Machine",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        212.0,
        anchor="nw",
        text="Node",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        264.0,
        anchor="nw",
        text="Release",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        316.0,
        anchor="nw",
        text="Version",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        400.0,
        160.0,
        1006.0,
        470.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        421.0,
        114.0,
        anchor="nw",
        text="Average Response Time",
        fill="#1E1E1E",
        font=("Inter", 25 * -1)
    )

    Home_Button = Button(
        bg = "#6489B4",
        text = "Home",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setHome(canvas,window),
        relief="flat"
    )
    Home_Button.place(
        x=18.0,
        y=0.0,
        width=117.0,
        height=56.0
    )

    Analyze_Button = Button(
        bg = "#6489B4",
        text = "Analyze",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setAnalyze(canvas,window),
        relief="flat"
    )
    Analyze_Button.place(
        x=150.0,
        y=0.0,
        width=155.0,
        height=56.0
    )

    Info_Button = Button(
        bg = "#6489B4",
        text = "Info",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    Info_Button.place(
        x=320.0,
        y=0.0,
        width=76.0,
        height=56.0
    )
    setInfoData(canvas)
    canvas.place(x = 0, y = 0)
    result = setInfoGraph(canvas,window,Home_Button,Analyze_Button)
    Home_Button.config(command = lambda: setHome(canvas,window))
    Analyze_Button.config(command = lambda: setAnalyze(canvas,window))
    if result == "H":
        Home_Button.invoke()
    elif result == "A":
        Analyze_Button.invoke()

def setAnalyze(canvas, window):
    canvas = Canvas(
    window,
    bg = "#6489B4",
    height = 582,
    width = 1041,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        56.0,
        1041.0,
        113.0,
        fill="#035C68",
        outline="")

    canvas.create_text(
        21.0,
        58.0,
        anchor="nw",
        text="Battery Analysis",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_rectangle(
        360.0,
        171.0,
        1020.0,
        545.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        490.0,
        113.0,
        anchor="nw",
        text="Battery Health Trend",
        fill="#1E1E1E",
        font=("Inter", 25 * -1)
    )

    canvas.create_text(
        21.0,
        189.0,
        anchor="nw",
        text="System Name",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        459.0,
        anchor="nw",
        text="Charge Capacity",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        513.0,
        anchor="nw",
        text="Cycle Count",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        405.0,
        anchor="nw",
        text="Design Capacity",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        351.0,
        anchor="nw",
        text="Chemistry",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        243.0,
        anchor="nw",
        text="Manufacturer",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        21.0,
        297.0,
        anchor="nw",
        text="Serial Number",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    Home_Button = Button(
        bg = "#6489B4",
        text = "Home",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setHome(canvas,window),
        relief="flat"
    )
    Home_Button.place(
        x=18.0,
        y=0.0,
        width=117.0,
        height=56.0
    )

    Analyze_Button = Button(
        bg = "#6489B4",
        text = "Analyze",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    Analyze_Button.place(
        x=150.0,
        y=0.0,
        width=155.0,
        height=56.0
    )

    Info_Button = Button(
        bg = "#6489B4",
        text = "Info",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setInfo(canvas, window),
        relief="flat"
    )
    Info_Button.place(
        x=320.0,
        y=0.0,
        width=76.0,
        height=56.0
    )
    setAnalyzeInfo(canvas,window)

def setGUI():
    window = Tk()
    window.geometry("1041x582")
    window.configure(bg = "#6489B4")

    canvas = Canvas(
        window,
        bg = "#6489B4",
        height = 582,
        width = 1041,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        56.0,
        1041.0,
        113.0,
        fill="#035C68",
        outline="")

    canvas.create_text(
        135.0,
        70.0,
        anchor="nw",
        text="Memory",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        488.0,
        70.0,
        anchor="nw",
        text="CPU",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_text(
        832.0,
        70.0,
        anchor="nw",
        text="Wi-Fi",
        fill="#FFFFFF",
        font=("Inter", 30 * -1)
    )

    canvas.create_rectangle(
        726.0,
        131.0,
        1020.0,
        316.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        404.0,
        399.0,
        anchor="nw",
        text="Usage",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        404.0,
        468.0,
        anchor="nw",
        text="Speed",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        404.0,
        534.0,
        anchor="nw",
        text="Processes",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        399.0,
        anchor="nw",
        text="In-Use",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        468.0,
        anchor="nw",
        text="Available",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        56.0,
        534.0,
        anchor="nw",
        text="Percent",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        387.0,
        131.0,
        681.0,
        370.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        48.0,
        131.0,
        342.0,
        370.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_text(
        726.0,
        320.0,
        anchor="nw",
        text="Send",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_text(
        726.0,
        543.0,
        anchor="nw",
        text="Recieve",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        726.0,
        352.0,
        1020.0,
        537.0,
        fill="#D9D9D9",
        outline="")

    Home_Button = Button(
        bg = "#6489B4",
        text = "Home",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    Home_Button.place(
        x=18.0,
        y=0.0,
        width=117.0,
        height=56.0
    )

    Info_Button = Button(
        bg = "#6489B4",
        text = "Info",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setInfo(canvas,window),
        relief="flat"
    )
    Info_Button.place(
        x=320.0,
        y=0.0,
        width=76.0,
        height=56.0
    )

    Analyze_Button = Button(
        bg = "#6489B4",
        text = "Analyze",
        font = font.Font(size=30),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: setAnalyze(canvas,window),
        relief="flat"
    )
    Analyze_Button.place(
        x=150.0,
        y=0.0,
        width=155.0,
        height=56.0
    )
    window.resizable(False, False)
    window.mainloop()
    return canvas
setGUI()
os._exit(0)