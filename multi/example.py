#!/usr/bin/python
# https://www.tutorialspoint.com/python/python_multithreading.htm

import thread
import time

# Function definitions
def print_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(str(name) + ": " + str(time.ctime(time.time())))


try:
    thread.start_new_thread(print_time, ("t1", 2, ))
    thread.start_new_thread(print_time, ("t2", 4, ))

except:
    print("ERROR: Unable to start thread")

while True:
    pass
