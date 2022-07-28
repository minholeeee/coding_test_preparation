from itertools import combinations
import sys
n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
result = 0
for length in range(1, n + 1):
    can = combinations(numbers, length)
    for c in can:
        if sum(list(c)) == s:
            result += 1
print(result)
