import psutil as ps
import platform
import subprocess
from bs4 import BeautifulSoup
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
import wmi

computer = wmi.WMI()
system_info = computer.Win32_ComputerSystem()[0]
print(f"Manufacturer: {system_info.Manufacturer}")
print(f"Model: {system_info.Model}")