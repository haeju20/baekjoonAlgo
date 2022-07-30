#1712
a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(int(a/(c-b) + 1))

#2292
N = int(input())
hex = 1
cnt = 1
while N > hex:
    hex += cnt * 6
    cnt += 1
print(cnt)

#1193
a = int(input())
l = 0 #한 줄에 같이 쓰면 안 됨
m = 0
while a > m:
    l += 1
    m += l
sub = m - a
if l % 2 == 0:
    num = l - sub
    den = sub + 1
else:
    num = sub + 1
    den = l - sub
print(f'{num}/{den}')

#2869
a, b, v = map(int, input().split())
day = (v-b)/(a-b)
if day == int(day):
    print(int(day))
else:
    print(int(day) + 1)

#10250
a = int(input())
for _ in range(a):
    h, w, n = map(int, input().split())
    room = (n//h) + 1
    floor = n % h
    if floor == 0:
        floor = h
        room -= 1
    print(floor * 100 + room)

#2775
T = int(input())
for _ in range(T):
    k = int(input()) #floor
    n = int(input()) #num
    fl = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            fl[j] += fl[j-1]
    print(fl[-1])

#2839


#10757
