#2609
import math
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))

#1934
import math
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    lcm = math.lcm(a, b)
    print(lcm)

#6588
import sys
li = [True for i in range(1000001)]
for i in range(2, 1001): #소수만 True인 리스트
    if li[i]:
        for j in range(i+i, 1000001, i):
            li[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, len(li)):
        if li[i] and li[n-i]:
            print(n, "=", i, "+", n-i)
            break

#1676
import math
n = int(input())
cnt = 0
for i in str(math.factorial(n))[::-1]:
    if i == '0':
        cnt += 1
    else:
        break
print(cnt)

#2004
def count(i, j):
    k = 0
    while i:
        i //= j
        k += i
    return k
    
n, m = map(int, input().split())
five_cnt = count(n, 5) - count(m, 5) - count(n-m, 5)
two_cnt = count(n, 2) - count(m, 2) - count(n-m, 2)
cnt = min(five_cnt, two_cnt)
print(cnt)
