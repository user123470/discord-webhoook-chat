#!/data/data/com.termux/files/usr/bin/bash

echo "[+] Installing Quantum DDoS Tool in Termux"
echo "[+] Updating packages..."
pkg update -y && pkg upgrade -y

echo "[+] Installing Python..."
pkg install python -y

echo "[+] Installing required packages..."
pkg install git -y
pkg install python-pip -y

echo "[+] Cloning repository..."
git clone https://github.com/RianModss/ddos-tools.git
cd ddos-tools

echo "[+] Setting up..."
chmod +x quantum_ddos.py
pip install --upgrade pip

echo "[+] Installation complete!"
echo "[+] Usage: python quantum_ddos.py"
echo "[+] Note: For educational purposes only!"
