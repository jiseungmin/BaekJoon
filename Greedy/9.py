t = int(input())

a,b,c = 0

while(True):
  if(t>=300):
    t=t-300
    a += 1
    continue
  if(t>=60):
    t = t-60
    b += 1
    continue
  if(t>=10):
    t = t-10
    c += 1
    continue
  if(t == 0):
    print(a,b,c)
    break
  if(t<10):
    print(-1)
    break