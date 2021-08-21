'''
a, b = input().split()
print(int(a) % int(b))

a=float(input())
print( format(a, ".2f") )
#format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다.

a, b = input().split()
b = float(a)/float(b)
print(format(b,".3f"))

a, b = input().split()

c = int(a) + int(b)
d = int(a) - int(b)
e = int(a) * int(b)
f = int(a) // int(b)
g = int(a) % int(b)
h = float(a) / float(b)

print(c)
print(d)
print(e)
print(f)
print(g)
print(format(h,".2f"))

a, b, c = input().split()

d = int(a) + int(b) + int(c)
e = (float(a) + float(b) + float(c)) / 3

print(d, format(e,".2f"))
'''

