import  threading
import time
import string
import random

def random_sign():
    signs = string.punctuation
    chosen_sign = random.choice(signs)
    return chosen_sign


def write_to_file(sign,file_to_write):
    file = open(file_to_write, "w")
    for _ in range(10000):
        file.write(sign)
    time.sleep(1)

def create_file():

    for num in range(1,11):
        sign = random_sign()
        th = threading.Thread(target=write_to_file, args=(sign,"file"+str(num)+".txt"))
        th.start()
    th.join()

start = time.perf_counter()
create_file()

stop = time.perf_counter()
print(f"Total Time : {stop-start}")