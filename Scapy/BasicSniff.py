from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP

def ip_send(pkt):
    print(pkt[IP].src)
    print(pkt[IP].dst)

def main():
    sniff(filter="ip", prn =ip_send)

if __name__ == "__main__":
    main()


