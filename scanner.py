#!/usr/bin/env python3
"""
Simple Port Scanner - Day 1 of 30-Day CyberSec Challenge
Scans common ports on target host to identify open services
"""
import socket
import sys
from concurrent.futures import ThreadPoolExecutor

# Common ports to scan
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 8080]

def scan_port(host, port):
    """Attempt connection to port and return status"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            return (port, "OPEN", service)
    except:
        pass
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <host>")
        sys.exit(1)
    
    host = sys.argv[1]
    print(f"\n[*] Scanning {host}...\n")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda p: scan_port(host, p), COMMON_PORTS)
    
    open_ports = [r for r in results if r]
    
    if open_ports:
        print(f"{'PORT':<10} {'STATE':<10} {'SERVICE'}")
        print("-" * 35)
        for port, state, service in sorted(open_ports):
            print(f"{port:<10} {state:<10} {service}")
    else:
        print("No open ports found")

if __name__ == "__main__":
    main()
