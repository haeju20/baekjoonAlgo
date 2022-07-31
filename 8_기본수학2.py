#1978
N = int(input())
num = map(int, input().split())
cnt = 0
for i in num:
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error == 0:
            cnt += 1
print(cnt)

#2581
M = int(input())
N = int(input())
p = []
for i in range(M, N+1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            p.append(i)
if len(p) > 0:
    print(sum(p))
    print(min(p))
else:
    print(-1)

#11653
N = int(input())
i = 2
while N != 1:
    if N % i == 0:
        N = N/i
        print(i)
    else:
        i += 1

#1929
M, N = map(int, input().split())
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)

#4948


#9020
