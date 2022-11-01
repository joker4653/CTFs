

import sys

if len(sys.argv) < 2:
    print("Usage: python3 hex_to_decimal.py [input]")
    sys.exit(1)
    
print(int(sys.argv[1], 16))