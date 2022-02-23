import os
netid = "192.168.1."
for hostid in range (1, 256):
        hostid=str(hostid)
        response = os.popen(f"ping {netid}{hostid} -c1")
        if "ttl" in response:
                print(netid+hostid)
