import numpy as np

# Some hashes
quotes = [b"Look how they massacred my boy",
          b"One does not simply walk into Mordor",
          b"It's a trap!",
          b"A fine addition to my collection",
          b"Another happy landing",
          b"Ya like jazz?"]


## hash function
def padding(B, m):
    if len(B) % m != 0:
        for i in range(m - len(B) % m):
            B.append(0)
    return B


def bitHash(P, bits):
    m = len(P)
    bits = padding(bits, m)
    N = len(bits) // m
    B = np.empty((N, m), dtype=int)
    for i in range(N):
        column = []
        for j in range(m):
            column.append(bits[i * m + j])
        B[i] = column
    for i in range(N):
        if i == 0:
            h = B[i]
        else:
            h = (h + B[i]) % 2
        h = np.matmul(P, h) % 2
    return h


def myHash(P, byteStr):
    bits = "{:b}".format(int(byteStr.hex(), 16))
    bithash = bitHash(P, list(bits))
    hsh = ''
    for i in range(len(bithash)):
        hsh += str(bithash[i])
    return "{:0{}x}".format(int(hsh, 2), len(P) // 4)


if __name__ == '__main__':
    # Load Matrix
    with open('key32.npy', 'rb') as f:
        P = np.load(f)
    print("Key Matrix:")
    print(P)
    print()

    for i in range(len(quotes)):
        print("Message: {}".format(quotes[i]))
        print("Hash: {}".format(myHash(P, quotes[i])))
        print()
    # Hash some file
    with open('key32.npy', 'rb') as f:
        sumthn = f.read()

    print("File: key32.npy")
    print("Hash: ", myHash(P, sumthn))