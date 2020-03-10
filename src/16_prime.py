import sys
import math

if len(sys.argv) != 2:
    print('Invalid usage. Correct usage is\n "python 16_prime.py <number>"')
else:
    final = 'prime'
    num = int(sys.argv[1])
    limit = int(math.sqrt(num))+1
    for i in range(2, limit):
        mod = num % i
        if mod == 0:
            final = 'composite'
            break
    print(f'Result: {final:s}')
