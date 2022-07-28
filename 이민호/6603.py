import sys
from itertools import combinations
while True:
    num = list(map(int, sys.stdin.readline().split()))
    if num[0] == 0:
        break
    can = combinations(num[1:], 6)
    for c in can:
        for i in range(len(c)):
            print(c[i], end=' ')
        print()
    print()
