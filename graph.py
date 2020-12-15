import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import json
import math

print('STARTING LOADING OF DATA...')
with open('out_floats.json') as file:
    data = json.load(file)
    print('FINISHED LOADING DATA FROM FILE')

print('BUILDING REAL DATA')
print(data[-100:])
print(math.isnan(data[-1]), data[-1])
print(math.isnan(data[0]), data[0])
real = []
for point in data:
    # if not math.isnan(point) and abs(point) != float('inf'):
    if not math.isnan(point) and abs(point) == point:
        real.append(point)
print(real[:100])
print(real[-100:])

print(f'Total original points: {len(data)}')
print(f'Total real points: {len(real)}')
print(f'Diff: {len(data) - len(real)}')
arr = np.array(real)
diffs = np.diff(real)
print(f'Min: {np.min(arr)}')
print(f'Max: {np.max(arr)}')

jumps = sorted(list(set(diffs)))
print(jumps)
print(len(jumps))

plt.plot(arr[1:], diffs)
plt.show()

