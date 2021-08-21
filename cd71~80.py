'''
while True:
  a = int(input())
  if (a == 0):
    break
  print(a)
n = int(input())
while True:
  print(n)
  n = n-1
  if(n == 0):
    break
n = int(input())
while True:
    n = n - 1
    print(n)
    if(n == 0):
     break

a = ord(input())
b = ord('a')#a의 정수값 출력
while b <= a:
    print(chr(b),end = ' ') # chr(정수값) 유니코드 문자로 출력 / end 마지막에 한칸만 띄운다 (\n 은 줄바꿈)
    b = b + 1

a = int(input())
b = 0
while b <= a:
    print(b, end = '\n')
    b = b + 1

a = int(input())
for i in range(a+1):
    print(i)



for i in range(n) :    #range(n)에 들어있는(in) 각각의 수에 대해서(for) 순서대로 i에 저장해 가면서...
이때의 for는 각각의 값에 대하여... 라는 for each 의 의미를 가진다고 생각할 수 있다.

range(끝)
range(시작, 끝)
range(시작, 끝, 증감)
형태로 수열을 표현할 수 있다. 시작 수는 포함이고, 끝 수는 포함되지 않는다. [시작, 끝)
증감할 수를 작성하지 않으면 +1이 된다.

반복 실행구조에 반복 횟수를 기록/저장하는 변수로 i를 자주 사용하는데,
i 는 반복자(iterator)를 나타내는 i라고 생각할 수 있다. i, j, k ... 알파벳 순으로 사용하기도 한다.

a = int(input())
sum = 0
for i in range(a + 1):
    if i % 2 == 0:
        sum = sum + i
print(sum)

while True:
    a = input()
    print(a)
    if a == 'q':
        break

a = int(input())
sum = 0
for i in range(a):
    sum = sum + i
    if sum >= a:
        print(i)
        break
a, b = map(int,input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print( i, j)

'''

a, b = map(int,input().split())
for i in range(1, a+1):
    for j in range(1, b+1):
        print( i, j)