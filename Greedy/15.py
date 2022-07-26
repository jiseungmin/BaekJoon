# 볼링공 고르기
from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))

w = list(combinations(data, 2))
count = len(w)

for i in w:
    if i[0] == i[1]:
        count -= 1

print(count)


# 방법1
n, m = map(int, input().split())  # n: 볼링공의 개수 m: 볼링공의 최대 무게
data = list(map(int, input().split()))  # n개의 공의 무게
result = 0

for i in range(n):
    for j in range(i, n):
        if data[i] != data[j]:
            result += 1

print(result)
