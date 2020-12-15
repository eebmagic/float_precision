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
    # int values of binary strings to start/end from
    start = 0

    # bit length to pad to
    bit_len = 32
    end = 2 ** bit_len 

    # int amount to skip by 
    skip = 512


    # Build set of bitstrings
    longString = make_strings(start, end, skip=skip)
    rows = longString.split('\n')

    strings = []
    ints = []
    floats = []

    # Build details of floats
    for row in tqdm(rows):
        padded = pad_string(row, bit_len)
        b = BitArray(bin=padded)
        strings.append(padded)
        ints.append(int_from_bits(row))
        floats.append(b.float)
    print(len(rows))


    # Save floats to file
    with open('out_floats.json', 'w') as file:
        json.dump(floats, file)
        print("FINISHED WRITING TO FILE")
