from tqdm import tqdm

def make_string(n):
    return "{0:b}".format(n)

def make_strings(start, stop):
    out = []
    for i in tqdm(range(start, stop)):
        out.append(make_string(i))
    
    return "\n".join(out)

def int_from_bits(instring):
    return int(instring, 2)

def pad_string(instring, size):
    out = instring
    while len(out) < size:
        out = "0" + out
    return out

if __name__ == "__main__":
    start = 0
    end = 4294967296
    bit_len = 32
    longString = make_strings(start, end)

    for row in longString.split('\n'):
        # print(row, int_from_bits(row))
        print(pad_string(row, bit_len), int_from_bits(row))
