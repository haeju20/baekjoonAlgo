#2739
a = int(input())
for i in range(1, 10):
    print(a, '*', i, '=', a*i)

#10950
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print(a+b)

#8393
n = int(input())
result = 0
for i in range(1, n+1):
    result += i
print(result)

#15552
import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

#2741
a = int(input())
for i in range(1, a+1):
    print(i)

#2742
a = int(input())
for i in range(a, 0, -1):
    print(i)

#11021
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print('Case #' + str(i) + ':', a+b)

#11022
T = int(input())
for i in range(1, T+1):
    a, b = map(int, input().split())
    print('Case #' + str(i) + ':', a, '+', b, '=', a+b)

#2438
a = int(input())
for i in range(1, a+1):
    print('*' * i)

#2439
a = int(input())
for i in range(1, a+1):
    print(' ' * (a-i) + '*' * i)

#10871
N, X = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] < X:
        print(A[i], end=" ")

#10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break;
    else:
        print(a+b)

#10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

#1110
a = int(input())
new = a
result = 0
while True:
    t = new//10
    u = new%10
    new = u*10 + (t+u)%10

    result += 1
    if new == a:
        break
print(result)
