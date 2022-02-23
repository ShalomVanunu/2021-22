import time

def show(sign,times,time_sleep):
    for x in range(times):
        print(sign*10)
        time.sleep(time_sleep)


start = time.perf_counter()
show("#",10,1) # all : 10 sec
show("*",10,0.5)  # all : 5 sec
# all 15 sec

stop = time.perf_counter()
print(f"Cycle Time of all  : {stop-start}")

