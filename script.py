from tqdm import tqdm
import json
from bitstring import BitArray

def make_strings(start, stop, skip=1):
    out = []
    for i in tqdm(range(start, stop, skip)):
        out.append("{0:b}".format(i))
    
    return "\n".join(out)

def int_from_bits(instring):
    return int(instring, 2)

def float_from_bits(instring):
    pass

def pad_string(instring, size):
    out = instring
    while len(out) < size:
        out = "0" + out
    return out

if __name__ == "__main__":
    # Set params for generation
    start = 0
    end = 4294967296
    bit_len = 32

    # Build set of bitstrings
    # longString = make_strings(start, end, skip=64)
    longString = make_strings(start, end, skip=512)
    rows = longString.split('\n')

    strings = []
    ints = []
    floats = []

    # Build details of floats
    for row in tqdm(rows):
        padded = pad_string(row, bit_len)
        b = BitArray(bin=padded)
        # print(padded, int_from_bits(row), b.float)
        strings.append(padded)
        ints.append(int_from_bits(row))
        floats.append(b.float)
    print(len(rows))


    # Save floats to file
    with open('out_floats.json', 'w') as file:
        json.dump(floats, file)
        print("FINISHED WRITING TO FILE")
