# 모험가 길드 문제
n = int(input())
people = list(map(int, input().split()))
people.sort()
result = 0
count = 0

for i in people:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
