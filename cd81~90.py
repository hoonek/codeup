'''
#6081
a = int(input(), 16)

for i in range(1,16):
    print('%x*%x=%x'%(a,i,a*i))

#6082
a = int(input())

for i in range(1,a+1):

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end=' ')

    else:
        print('%d'%(i), end=' ')

#6083
r, g, b = map(int,input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i,j,k)

a = r * g * b
print(a)

#6084
h,b,c,s = map(int,input().split())
m = (h* b * c * s)/8/1024/1024
print('%.1f MB' %m)

#6085
w,h,b = map(int,input().split())
m = (w* h * b )/8/1024/1024
print('%.2f MB' %m)

#6086
a = int(input())
s = 0
c = 1
while True:

    s = s + c
    c = c + 1
    if s>=a:
        break

print(s)

#6087
a = int(input())

for i in range(1,a+1):
    if i%3 != 0:
        print(i,end= (' '))

#6088
a, d, n = map(int,input().split())
s = a + (n-1)*d
print(s)

#6089
a, r, n = map(int,input().split())
s = a*r**(n-1)
print(s)

#6090
a, m, d, n = map(int,input().split())
s=a
for i in range(0,n-1):
    s = s*m+d

print(s)
'''

a, m, d, n = map(int,input().split())
s=a
for i in range(0,n-1):
    s = s*m+d

print(s)