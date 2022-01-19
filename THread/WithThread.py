import time
import threading

def run_numbers():
    print("No.1")
    time.sleep(3)
    print("No.2")

th = threading.Thread(target=run_numbers)
th.start()
print("No.3")