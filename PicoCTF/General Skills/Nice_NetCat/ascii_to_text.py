# simple program to convert ascii to text
# 1/11/2022

import sys


with open(sys.argv[1]) as file:
    for line in file:
            print(chr(int(line)), end = "")