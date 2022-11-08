
# PicoCTF Challenge -> decoding using given scheme
# mod 37 each number then assign it a value based of the answer, 0-> 25 is alphabet (uppercase), 26->35 are decimal digits, 36 is _


import sys

fileName = None
numbers = []
mapper = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H', 8 : 'I', 9 : 'J', 10 : 'K', 11 : 'L', 12 : 'M', 13 : 'N', 14 : 'O' , 15 : 'P',
         16 : 'Q', 17 : 'R', 18 : 'S', 19 : 'T', 20 : 'U', 21 : 'V', 22 : 'W', 23 : 'Y', 24 : 'X', 25 : 'Z', 26 : '0', 27 : '1', 28 : '2', 29 : '3', 30 : '4', 31 : '5', 32 : '6', 33 : '7',
         34 : '8', 35 : '9', 36 : '_'}

def build_decoded(numbers):
    decoded = ''
    for num in numbers:
        decoded += decoded.join(mapper[num])

    print(decoded)


if len(sys.argv) < 2:
    print(f"Correct Usage: python3 {sys.argv[0]} [file]")
else:
    fileName = sys.argv[1]


with open(fileName, "r") as f:
    for num in f.read().strip().split(' '):
        # mod the number first
        numbers.append((int(num) % 37))
    
    build_decoded(numbers)