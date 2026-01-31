#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Quantum DDoS Tool - Educational')
parser.add_argument('--target', required=True, help='Target IP/Domain')
parser.add_argument('--port', type=int, default=80, help='Target port')
parser.add_argument('--method', choices=['TCP','UDP','HTTP','SLOWLORIS'], default='TCP')
parser.add_argument('--threads', type=int, default=100)
parser.add_argument('--time', type=int, default=60, help='Duration in seconds')
parser.add_argument('--size', type=int, default=1024, help='Packet size')

args = parser.parse_args()

# Implementasi attack sama seperti script utama
# ... (code dari quantum_ddos.py)
