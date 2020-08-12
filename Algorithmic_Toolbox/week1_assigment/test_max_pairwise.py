import random
import sys
n = int(sys.argv[1])
print(n)
print(' '.join([str(i) for i in random.sample(range(n//2, n*2), n)]))
