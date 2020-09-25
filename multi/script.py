# threading_simpleargs.py
import threading
import sys
import time
time_start = time.time()

def makestr(n):
    return "{0:b}".format(n)

def padstr(s, size):
    out = s
    while len(out) < size:
        out = "0" + out
    return out

def worker(num, start, end, padsize, out):
    """thread worker function"""
    print('Starting: %s' % num)
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
thread_count = 14

padsize = 22
for entry in sys.argv:
    try:
        padsize = int(entry)
    except:
        pass

end = 2 ** padsize
chunk_size = end // thread_count
time_estimation = 1.2 * (end / 1_000_000)
print("chunk size: " + str(chunk_size))
print("btr len: " + str(padsize))
print("end: " + str(end))
print("estimated time: " + str(time_estimation))
print("estimaged mins: " + str(time_estimation / 60))
print("")

try:
    cont = input("Continue? (Y/n): ").strip().lower()
    if "n" in cont:
        print("Quiting...")
        quit()
except KeyboardInterrupt:
    print("")
    quit()

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

opdurr = time.time() - time_start
tpd = (opdurr / end) * 1_000_000
print("time per million entries: " + str(tpd))

# wideprint(record, 6)
print("total of entries in record: " + str(len(record)))

if "-f" in sys.argv:
    print("writing to file...")
    file_start = time.time()
    final_str = '\n'.join([str(x) for x in record])
    with open("output.txt", 'w') as file:
        file.write(final_str)
    file_durration = time.time() - file_start

duration = time.time() - time_start
print("total time: " + str(duration))

if "-f" in sys.argv:
    print("time without file: " + str(duration - file_durration))
