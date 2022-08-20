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


#10809


#10820


#2743


#11655


#10824


#11656
