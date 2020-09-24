# threading_simpleargs.py
import threading
import time
start = time.time()

def makestr(n):
    return "{0:b}".format(n)

def padstr(s, size):
    out = s
    while len(out) < size:
        out = "0" + out
    return out

def worker(num, start, end, padsize, out):
    """thread worker function"""
    print("start: " + str(start))
    print("stop: " + str(stop))
    for i in range(start, end):
        s = padstr(makestr(i), padsize)
        out.append((i, s))
    print('Finished: %s' % num)

def wideprint(l, width):
    for i in range(len(l)):
        if i % width == 0:
            print("\n")
        else:
            print(l[i], end=' ')
    print("")

threads = []
thread_count = 5

padsize = 8
end = 2 ** padsize
chunk_size = end // thread_count
print("chunk size: " + str(chunk_size))
print("btr len: " + str(padsize))
print("end: " + str(end))
record = []
for i in range(thread_count):
    start, stop = chunk_size*i, chunk_size*(i+1)
    t = threading.Thread(target=worker, args=(i, chunk_size*i, chunk_size*(i+1), padsize, record,))
    threads.append(t)
    t.start()

# Check for live threads still
still_live = True
while still_live:
    still_live = False
    for t in threads:
        if t.is_alive():
            still_live = True

# worker(-1, end, end+1, padsize, record)

# wideprint(record, 6)
print("total of entries in record: " + str(len(record)))

final_str = '\n'.join([str(x) for x in record])
with open("output.txt", 'w') as file:
    file.write(final_str)

duration = time.time() - start
print("total time: " + str(duration))
