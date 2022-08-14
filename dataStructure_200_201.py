#10828
import sys
num = int(sys.stdin.readline())
S = []
for i in range(num):
    comm = sys.stdin.readline().split()
    if comm[0] == 'push':
        S.append(comm[1])
    elif comm[0] == 'pop':
        if len(S) == 0:
            print(-1)
        else:
            print(S.pop())
    elif comm[0] == 'size':
        print(len(S))
    elif comm[0] == 'empty':
        if len(S) == 0:
            print(1)
        else:
            print(0)
    elif comm[0] == 'top':
        if len(S) == 0:
            print(-1)
        else:
            print(S[-1])

#9093
import sys
T = int(sys.stdin.readline())
for i in range(T):
    sent = sys.stdin.readline().rstrip()
    w = list(sent.split())
    rev_w = []
    for j in w:
        rev_w.append(j[::-1])
    result = " ".join(rev_w)
    print(result)

#9012
import sys
T = int(sys.stdin.readline())
for i in range(T):
    par = sys.stdin.readline()
    par = list(par)
    result = 0
    for j in par:
        if j == '(':
            result += 1
        elif j == ')':
            result -= 1
        if result < 0:
            print('NO')
            break
    if result > 0:
        print('NO')
    elif result == 0:
        print('YES')

#1874
n = int(input())
S = []
result = []
cnt = 1
flag = True
for _ in range(n):
    num = int(input())
    while cnt <= num:
        S.append(cnt)
        result.append('+')
        cnt += 1
    if S[-1] == num:
        S.pop()
        result.append('-')
    else:
        flag = False
if flag == False:
    print('NO')
else:
    for i in result:
        print(i)

#1406
import sys
S = list(sys.stdin.readline().rstrip())
t = []
for _ in range(int(sys.stdin.readline())):
    comm = list(sys.stdin.readline().split())
    if comm[0] == 'L':
        if S:
            t.append(S.pop())
    elif comm[0] == 'D':
        if t:
            S.append(t.pop())
    elif comm[0] == 'B':
        if S:
            S.pop()
    else:
        S.append(comm[1])
S.extend(reversed(t))
print("".join(S)) 

#10845


#1158


#10866


#17413
import sys
S = list(sys.stdin.readline().rstrip())
i = 0
start = 0
while i < len(S):
    if S[i] == '<':
        i += 1
        while S[i] != '>':
            i += 1
        i += 1 #'>' 만나면 인덱스 증가
    elif S[i].isalnum():
        start = i
        while i < len(S) and S[i].isalnum(): #isalnum() 영어/한글/숫자라면 참
            i += 1
        #문자열 뒤집기
        N = S[start:i]
        N.reverse()
        S[start:i] = N
    else:
        i += 1

print("".join(S))

#10799
par = list(input())
S = [] #stack
num = 0
for i in range(len(par)):
    if par[i] == '(':
        S.append('(')
    else:
        if par[i-1] == '(':
            S.pop()
            num += len(S)
        else:
            S.pop()
            num += 1
print(num)

#17298


#17299
