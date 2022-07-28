from collections import deque
import sys
test_cases = int(sys.stdin.readline())
for _ in range(test_cases):
    n, m = map(int, sys.stdin.readline().split())
    prior = deque(list(map(int, sys.stdin.readline().split())))
    number_list = deque([i for i in range(n)])

    how_many = 0
    while True:
        if prior[0] == max(prior):
            prior.popleft()
            now = number_list.popleft()
            how_many += 1
            if now == m:
                print(how_many)
                break
        else:
            prior.rotate(-1)
            number_list.rotate(-1)
