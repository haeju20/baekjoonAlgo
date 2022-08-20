#1935
N = int(input())
post = input()
s = []
opd_li = [0] * N
for i in range(N):
    opd_li[i] = int(input())
for j in post:
    if j.isalpha():
        s.append(opd_li[ord(j)-65])
    else:
        opd2 = s.pop()
        opd1 = s.pop()
        if j == '+':
            s.append(opd1 + opd2)
        elif j == '-':
            s.append(opd1 - opd2)
        elif j == '*':
            s.append(opd1 * opd2)
        elif j == '/':
            s.append(opd1 / opd2)
print('%0.2f' %s[0])

#1918
infix = list(input())
s = [] #stack
postfix = ''
for i in infix:
    if i.isalpha(): #알파벳이면 추가
        postfix += i
    else: #알파벳이 아니면
        if i == '(':
            s.append(i)
        elif i == '*' or i == '/':
            while s and (s[-1] == '*' or s[-1] == '/'):
                postfix += s.pop()
            s.append(i)
        elif i == '+' or i == '-':
            while s and s[-1] != '(':
                postfix += s.pop()
            s.append(i)
        elif i == ')':
            while s and s[-1] != '(':
                postfix += s.pop()
            s.pop()
while s:
    postfix += s.pop()
print(postfix)

#10808
S = input()
li = [0] * 26
for i in S:
    li[ord(i) - ord('a')] += 1
print(*li)

#10820
import sys
while True:
    st = sys.stdin.readline().rstrip('\n')
    if not st:
        break
    l, u, n, sp = 0, 0, 0, 0
    for each in st:
        if each.islower():
            l += 1
        elif each.isupper():
            u += 1
        elif each.isdigit():
            n += 1
        elif each.isspace():
            sp += 1
    print(l, u, n, sp)

#2743
s = input()
print(len(s))

#11655
s = input()
enc = ''
for i in s:
    if i.islower():
        i = ord(i) + 13
        if i > 122:
            i -= 26
        enc += chr(i)
    elif i.isupper():
        i = ord(i) + 13
        if i > 90:
            i -= 26
        enc += chr(i)
    else:
        enc += i
print(enc)

#10824
A, B, C, D = map(str, input().split())
AB = A + B
CD = C + D
print(int(AB) + int(CD))

#11656
