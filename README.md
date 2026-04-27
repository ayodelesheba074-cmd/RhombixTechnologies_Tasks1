OVERVIEW
. This network sniffer tool is a Python-based utility designed to capture and analyze live traffic on the en0 interface. It provides real time visibility into network communications for monitoring and debugging purposes.

FEATURES
. Captures network packets specifically on the en0 interface.
. Identifies and displays Source and Destination IP addresses.
. Display protocols including TCP,UDP,and ICMP
. Records precise timestamps for every captured packets
. Automatically saves all captured data to a file called sniffer_log.txt for review later 

PREQUISITES
To use this tool, you must have the Scapy library installed.
. pip install scapy

HOW TO RUN IT 
. Due to the nature of network packet capturing, the script requires administrative privileges.
. Run the script: sudo python3 sniffer.py
