# threading_simpleargs.py
import threading

def makestr(n):
    return "{0:b}".format(n)

def padstr(s, size):
    out = s
    while len(out) < size:
        out = "0" + out
    return out

def worker(num, start, end, out):
    """thread worker function"""
    print('Worker: %s' % num)
    for i in range(start, end):
        s = padstr(makestr(i), 32)
        out.append(s)
    print('Finished: %s' % num)


threads = []
record = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i, 100*i, 100*(i+1), record,))
    threads.append(t)
    t.start()

print(record)
