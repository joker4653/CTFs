
import base64
import sys
import codecs


if len(sys.argv) < 2:
    print("Usage: python3 bases.py [encode string]")
    sys.exit(1)

b64Str = codecs.encode(sys.argv[1])
resStr = base64.b64decode(b64Str)

print(resStr)
