# Nmap XML to Excel Converter

This Python tool converts Nmap scan results (XML output) into a structured Excel (`.xlsx`) file.  
It is designed for penetration testers, network administrators, and security analysts who want to quickly generate readable reports from raw Nmap scans.

---

## 📌 Features
- Converts **Nmap XML output** into Excel format
- Lists hosts with their **IP/Hostname** and detected **open ports**
- Auto-generates a clean table:

- Supports saving:
- With the **same name as XML** (e.g., `scan.xml → scan.xlsx`)
- With a **timestamp** to avoid overwriting (optional)

---

## 📦 Requirements
- Python 3.8+
- [openpyxl](https://pypi.org/project/openpyxl/)

Install dependencies:

```bash
pip install openpyxl

```
---

## Usage

- Step 1: Generate Nmap XML output

Run your Nmap scan and save the results in XML format

- Step 2: Convert XML to Excel

Run the script:
```
python ip_sort.py scan_results.xml
```
- Step 3: Get the Excel report

The Excel file will be created in the same folder.

---


Thank me later :) 

## 👨‍💻 Author

**Venkatraj Kannan**
