#!/usr/bin/env python3

import sys
import socket

def resolve_subdomain(subdomain):
    try:
        return socket.gethostbyname(subdomain)
    except socket.gaierror:
        return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 subdomain_enum.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"\n[*] Enumerating subdomains for {domain}\n")

    with open("wordlist.txt", "r") as f:
        for word in f:
            sub = f"{word.strip()}.{domain}"
            ip = resolve_subdomain(sub)
            if ip:
                print(f"[+] {sub:<25} -> {ip}")

if __name__ == "__main__":
    main()
