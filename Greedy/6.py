#1541번 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
#그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
#괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

a = input().split('-') # 입력값을 -로 나누어준다. 55+10-50+40 => [55,(50+40)]
sum = 0

for i in a[0].split('+'): # 최초로 나오는 마이너스 전까지는 더해줄수밖에 없기때문에 첫번째에 들어 있는 수는 다 더해줘야함
  sum += int(i)

for i in a[1:]:
  for j in i.split('+'): # 그 뒤에 있는 수들을 +로 나누고 sum을 빼줌
    sum -= int(j)  

print(sum)    