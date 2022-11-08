
# PicoCTF Challenge -> decoding using given scheme
# mod 37 each number then assign it a value based of the answer, 0-> 25 is alphabet (uppercase), 26->35 are decimal digits, 36 is _


import sys
import string

fileName = None
flag = []
if len(sys.argv) < 2:
    print(f"Correct Usage: python3 {sys.argv[0]} [file]")
else:
    fileName = sys.argv[1]


with open(fileName, "r") as f:
    file = f.read()
    numbers = [int(val) for val in file.split()]
    
    for n in numbers:
        mod = pow(n, -1, 41)

        if mod in range(1,27):
            # then uppercase alphabet
            flag.append(string.ascii_uppercase[mod - 1])
        elif mod in range(27, 37):
            flag.append(string.digits[mod - 27])
        else:
            flag.append("_")

print("picoCTF{%s}" % "".join(flag))