n, k = map(int, input().split())
robots = []
up_load = 0
down_load = n - 1
belt = list(map(int, input().split()))
day = 0

###주의! 컨베이어벨트가 회전할때도 로봇들이 한 칸 이동합니다!
while (True):
    up_load += 2 * n - 1
    down_load += 2 * n - 1

    for i in range(len(robots)):
        if belt[(robots[i] + 1) % (2 * n)] >= 1:
            if len(list(filter(lambda x: x % (2 * n) == (robots[i] + 1) % (2 * n), robots))) == 0:
                #다음 위치에 로봇 있으면 멈춤
                robots[i] += 1
                belt[robots[i] % (2 * n)] -= 1

    if belt[up_load % (2 * n)] >= 1:
        robots.append(up_load % (2 * n))
        belt[up_load % (2 * n)] -= 1
    if robots.count(down_load % (2 * n)) != 0:
        robots.remove(down_load % (2 * n))
    print(robots)
    print(belt)
    day += 1
    if belt.count(0) >= k:
        break

    print(up_load % (2 * n))
    print(down_load % (2 * n))
print(day)
import sys

input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * n)
res = 0

while 1:
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0  # 로봇이 내려가는 부분이니 0
    if sum(robot):  # 로봇이 존재하면
        for i in range(n - 2, -1, -1):  # 로봇 내려가는 부분 인덱스 i-1 이므로 그 전인 i-2부터
            if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1] >= 1:
                robot[i + 1] = 1
                robot[i] = 0
                belt[i + 1] -= 1
        robot[-1] = 0  # 이 부분도 로봇 out -> 0임
    if robot[0] == 0 and belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
    res += 1
    print(belt)
    if belt.count(0) >= k:
        break

print(res)
