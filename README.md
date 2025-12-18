Basic Port Scanner (Python)

A simple multi-threaded TCP port scanner written in Python.  
This tool identifies open ports on a target host using TCP connect scanning
(similar to `nmap -sT`).

---

## 🎯 Purpose

The goal of this project is to demonstrate:
- basic network reconnaissance
- TCP connect-based port scanning
- concurrent scanning using Python threads
- clean CLI-style output

This is intended for **learning and controlled testing environments only**.

---

## 🔧 Features

- Scans a predefined list of common TCP ports
- Uses multi-threading for faster execution
- Identifies basic services for open ports
- Simple and readable implementation
- No external dependencies (Python standard library only)

---

## 🧩 How It Works (High Level)

1. Target hostname is provided as a command-line argument
2. The script attempts TCP connections to common ports
3. Open ports are identified based on successful connections
4. Results are displayed in a tabular CLI format

---

## 🚀 Usage

### Prerequisites
- Python 3.x installed

### Run the scanner
```bash
python3 scanner.py <target>
