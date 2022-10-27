from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP,Ether

def show(pkt):
    if (pkt[Ether].dst == "ff:ff:ff:ff:ff:ff"):
        print(pkt.show())
        print(pkt[IP].src)

def main():
    #172.20.129.27
    sniff(filter="ip", prn = show)

if __name__ == "__main__":
    main()