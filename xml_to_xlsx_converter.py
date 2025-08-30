import xml.etree.ElementTree as ET
import openpyxl
from datetime import datetime
import os

# Input file
nmap_xml_file = r"<xml_file_path>"

# Output file with timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
base_name = os.path.splitext(os.path.basename(nmap_xml_file))[0]
output_xlsx_file = f"{base_name}_{timestamp}.xlsx"

# Parse the Nmap XML
tree = ET.parse(nmap_xml_file)
root = tree.getroot()

# Create a workbook and worksheet
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Nmap Results"

# Write header row
sheet.append(["S.No", "Host Name/IP", "Open Ports"])

# Iterate through hosts
serial_no = 1
for host in root.findall("host"):
    addr = host.find("address")
    ip = addr.get("addr") if addr is not None else "N/A"

    open_ports = []
    for port in host.findall(".//port"):
        state = port.find("state")
        if state is not None and state.get("state") == "open":
            open_ports.append(port.get("portid"))

    if open_ports:
        sheet.append([serial_no, ip, ",".join(open_ports)])
        serial_no += 1

# Save Excel file
workbook.save(output_xlsx_file)
print(f"[+] Results saved to {output_xlsx_file}")

#Thank me later :) Venkatraj Kannan
