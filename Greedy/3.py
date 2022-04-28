a,b = map(int,input().split())
cnt = 0
money = []
for i in range(a):
  money.append(int(input()))
money.sort()
money.reverse()

for i in range(0,a-1):
  if b > money[i]:
    cnt += b // money[i]
    b = b % money[i]

print(cnt)


