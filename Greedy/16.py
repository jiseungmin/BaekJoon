# 회의실 배정 문제
n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start, end])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
count = 0

for i, j in time:
    if last <= i:
        count += 1
        last = j
