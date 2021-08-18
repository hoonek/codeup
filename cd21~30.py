'''
a = input()
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

s = input()
print(s[0:2] + ' '+s[2:4] + ' ' + s[4:6])

a = input().split(':')
print(a[1])

w1, w2 = input().split()
s = w1 + w2
print(s)

a, b = input().split()
c = int(a) + int(b)
print(c)

a = float(input())
b = float(input())
print(a + b)

a = input()
n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력

a = input()
n = int(a)
print('%X'% n)

a = input()
n = int(a, 16)      #입력된 a를 16진수로 인식해 변수 n에 저장
print('%o' % n)  #n에 저장되어있는 값을 8진수(octal) 형태 문자열로 출력

n = ord(input())
print(n)
#ord: 문자를 10진수로 변환
'''


