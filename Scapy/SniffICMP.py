from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP

def show(pkt):
    if "172.20.149" in pkt[IP].src:
        print(f"packet is LAN", pkt[IP].src)

def main():
    #172.20.129.27
    sniff(filter="icmp", prn = show)

if __name__ == "__main__":
    main()