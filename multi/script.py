import time
import threading

def adder(name, start, end, out):
    print(name + " is starting.")
    start = time.time()
    print("start: " + str(start))
    print("start as int: " + str(int(start)))
    for i in range(start, end):
        out.append(i)
        print("adding number")
    
    duration = time.time() - start
    print(name + " finished in " + str(duration) + " seconds.")


record = []

print("before: " + str(record))

x = threading.Thread(target=adder, args=["one", 0, 100, record])
x.start()

print("after: " + str(record))
