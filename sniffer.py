from scapy.all import *
from datetime import datetime

print("Starting network sniffer...")

def packet_callback(packet):
    if packet.haslayer(IP):
        protocols = {6: "TCP", 17: "UDP", 1: "ICMP"}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto_num = packet[IP].proto
        proto_name = protocols.get(proto_num, str(proto_num))

        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {proto_name}")
        output = f"[{timestamp}] Source {src_ip} -> {dst_ip} | Protocol: {proto_name}"

        with open("sniffer_log.txt", "a") as f:
            f.write(output + "\n")

sniff(iface="en0", prn=packet_callback, count=10)