Overview
This network sniffer tool is a Python-based utility designed to capture and analyze live traffic on the en0 interface. It provides real-time visibility into network communications for monitoring and debugging purposes.

Features
Captures network packets specifically on the en0 interface.

Identifies and displays Source and Destination IP addresses.

Detects and labels protocols including TCP, UDP, and ICMP.
Overview
This network sniffer tool is a Python-based utility designed to capture and analyze live traffic on the en0 interface. It provides real-time visibility into network communications for monitoring and debugging purposes.

Features
Captures network packets specifically on the en0 interface.

Identifies and displays Source and Destination IP addresses.

Detects and labels protocols including TCP, UDP, and ICMP.

Logs precise timestamps for every captured packet.

Automatically saves all session data to a local file named sniffer_log.txt.

Prerequisites
To use this tool, you must have the Scapy library installed.

pip install scapy

How to Run
Capturing network packets requires administrative privileges. Use sudo to execute the script.

sudo python3 sniffer.py
