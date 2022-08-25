#9613
import math
t = int(input())
for _ in range(t):
    s = 0
    num = list(map(int, input().split()))
    for i in range(1, len(num)):
        for j in range(i+1, len(num)):
            s += math.gcd(num[i], num[j])
    print(s)

#17087
import math
n, s = map(int, input().split())
a = list(map(int, input().split()))
dis = list(set(abs(a[i] - s) for i in range(n)))
d = min(dis)
for i in range(len(dis)):
    d = math.gcd(dis[i], d)
print(d)

#1373
print(oct(int(input(),2))[2:])

#1212
print(bin(int(input(), 8))[2:])

#2089


#17103
