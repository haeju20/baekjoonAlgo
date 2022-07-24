#1330
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')

#9498
a = int(input())
if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')

#2753
a = int(input())
if ((a%4) == 0 and (a%100) != 0) or (a%400) == 0:
    print('1')
else:
    print('0')

#14681
a = int(input())
b = int(input())
if a > 0 and b > 0:
    print('1')
elif a < 0 and b > 0:
    print('2')
elif a < 0 and b < 0:
    print('3')
else:
    print('4')

#2884
a, b = map(int, input().split())
if b >= 45:
    print(a, b-45)
elif a != 0 and b < 45:
    print(a-1, (b+60)-45)
else:
    print(23, (b+60)-45)

#2525
a, b = map(int, input().split())
c = int(input())
h = int((b+c)/60)
m = (b+c)%60
if b+c < 60:
    print(a, b+c)
elif a+h < 24 and b+c >= 60:
    print(a+h, m)
else:
    print(a+h - 24, m)

#2480
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)
