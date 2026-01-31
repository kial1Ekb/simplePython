from scapy.all import sniff, TCP, IP
import socket
from datetime import datetime

GRUYERE_HOST = "google-gruyere.appspot.com"
GRUYERE_IP = socket.gethostbyname(GRUYERE_HOST)

LOG_FILE = "traffic_log.txt"

print(f"Перехват трафика для {GRUYERE_HOST} ({GRUYERE_IP})")
print(f"Сохранение в файл: {LOG_FILE}")
print("="*60)

with open(LOG_FILE, "w") as f:
    f.write(f"Лог трафика Google Gruyere\n")
    f.write(f"Дата: {datetime.now()}\n")
    f.write(f"Хост: {GRUYERE_HOST} ({GRUYERE_IP})\n")
    f.write("="*60 + "\n\n")
    f.flush()

def packet_callback(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        if GRUYERE_IP not in (src_ip, dst_ip):
            return

        src = f"{src_ip}:{packet[TCP].sport}"
        dst = f"{dst_ip}:{packet[TCP].dport}"
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]

        output = f"\n[{timestamp}] [{src}] -> [{dst}]\n"
        output += f"Flags: {packet[TCP].flags}\n"

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            output += f"Данные ({len(payload)} байт):\n"
            try:
                decoded = payload.decode('utf-8', errors='ignore')
                output += decoded + "\n"
            except:
                output += str(payload[:500]) + "\n"

        print(output)

        try:
            with open(LOG_FILE, "a") as f:
                f.write(output)
                f.write("-"*60 + "\n")
                f.flush()
        except Exception as e:
            print(f"Ошибка записи в файл: {e}")

sniff(filter="tcp port 80", prn=packet_callback, store=0)
