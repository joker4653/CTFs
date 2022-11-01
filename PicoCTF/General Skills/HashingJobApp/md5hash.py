
import hashlib
import sys




r = hashlib.md5(sys.argv[1].encode())

print(r.digest())


