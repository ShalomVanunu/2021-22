from scapy.all import *
from scapy.layers.inet import TCP,IP,ICMP

Webname = "www.rotter.net"

packet = IP(dst= Webname, ttl = 5) / TCP()

answer = sr1(packet)
print(answer.show())


