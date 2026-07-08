## Overview
This network sniffer tool is a Python-based utility designed to capture and analyze live traffic on the en0 interface. It provides real time visibility into network communications for monitoring and debugging purposes.

## Features
* Captures network packets specifically on the en0 interface
* Identifies and displays Source and Destination IP addresses
* Displays protocols including TCP, UDP, and ICMP
* Records precise timestamps for every captured packet
* Automatically saves all captured data to a file called sniffer_log.txt for later review

## Prerequisites
To use this tool, you must have the Scapy library installed.

'pip install scapy'

## How to Run It
Due to the nature of network packet capturing, the script requires administrative privileges. Run the script using the command below.

'sudo python3 sniffer.py'
