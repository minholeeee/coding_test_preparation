import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    command = sys.stdin.readline()
    n = int(sys.stdin.readline())
    tmp = sys.stdin.readline()
    X = deque(list((tmp[1:len(tmp) - 2]).split(',')))
    error = False
    if len(X) == 1 and X[0] == '':
        X = []
        if 'D' in command:
            print('error')
            continue
    is_reverse = False
    for c in command:
        if c == 'R':
            if X:
                if is_reverse:
                    is_reverse = False
                else:
                    is_reverse = True
        if c == 'D':
            if len(X) != 0:
                if is_reverse:
                    X.pop()
                else:
                    X.popleft()
            else:
                error = True
                break
    if is_reverse:
        X.reverse()
    if error:
        print('error')
    else:
        print("[" + ",".join(list(X)) + "]")
