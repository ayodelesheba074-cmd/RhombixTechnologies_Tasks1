from scapy.all import sniff, IP, TCP, UDP
from datetime import datetime

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        src_port = "N/A"
        dst_port = "N/A"

        if packet.haslayer(TCP):
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            protocol_name = "TCP"
        elif packet.haslayer(UDP):
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            protocol_name = "UDP"
        else:
            protocol_name = str(proto)

        log_entry = f"[{timestamp}] {src_ip}:{src_port} -> {dst_ip}:{dst_port} | Proto: {protocol_name}\n"
        print(log_entry.strip())
        
        with open("sniffer_log.txt", "a") as f:
            f.write(log_entry)

print("Starting sniffer with TCP Port 443 filter...")
sniff(iface="en0", filter="tcp port 443", prn=packet_callback, store=0)