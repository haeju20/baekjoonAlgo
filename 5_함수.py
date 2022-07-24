#15596
def solve(a):
    ans = 0
    ans = sum(a)
    return ans

#4673
n = list(range(1, 10001))
r = []
for i in n:
    for j in str(i):
        i += int(j)
    if i <= 10000:
        r.append(i)
r = set(r)
a = [x for x in n if x not in r]
for i in a: #print(*a, sep='\n')
    print(i)

#1065
a = int(input())
cnt = 0
for i in range(1, a+1):
    if i < 100:
        cnt += 1
    else:
        j = list(map(int, str(i)))
        if j[2] - j[1] == j[1] - j[0]:
                cnt += 1
print(cnt)
