#2750
N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))
li = sorted(li)
for i in range(N):
    print(li[i])

#2751
import sys
N = int(input())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
li = sorted(li)
for i in li:
    print(i)

#10989


#2108
import sys
from collections import Counter
n = int(sys.stdin.readline())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()
li_s = Counter(nums).most_common()
print(round(sum(nums) / n))
print(li[n // 2])
if len(li_s) > 1:
    if li_s[0][1] == li_s[1][1]:
        print(li_s[1][0])
    else:
        print(li_s[0][0])
else:
    print(li_s[0][0])
print(li[-1] - li[0])

#1427
n = int(input())
li = []
li = list(map(int,str(n)))
li.sort(reverse=True)
for i in li:
    print(i,end='')

#11650
import sys
N = int(sys.stdin.readline())
co = []
for _ in range(N):
    co.append(list(map(int, sys.stdin.readline().split())))
co.sort(key=lambda x: (x[0], x[1]))
for i in co:
    print(i[0], i[1])

#11651
import sys
N = int(sys.stdin.readline())
co = []
for _ in range(N):
    co.append(list(map(int, sys.stdin.readline().split())))
co.sort(key=lambda x: (x[1], x[0]))
for i in co:
    print(i[0], i[1])

#1181
import sys
N = int(sys.stdin.readline())
li = []
for i in range(N):
    li.append(sys.stdin.readline().strip())
li = list(set(li))
li.sort()
li.sort(key = len)
for i in li:
    print(i)

#10814


#18870
