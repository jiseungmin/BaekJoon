# 만들수 없는 금액
n = int(input())

coin = list(map(int, input().split()))
coin.sort()  # 3 5 7

target = 1

for i in coin:
    if target < i:
        break
    target += coin

print(target)
