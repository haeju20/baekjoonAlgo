#11654
a = input()
print(ord(a))

#11720
n = input()
a = input()
s = 0
s = [int(i) for i in str(a)] #sum(map(int, input()))
print(sum(s))

#10809
S = input()
for i in range(97, 123):
    ch = chr(i)
    if ch not in S:
        print('-1')
    else:
        print(S.index(ch)) #find() 찾는 문자 없으면 -1 반환

#2675
T = int(input())
for i in range(T):
    R, S = input().split() #한 줄에서 입력받아야 하는데
    #R = int(input()) -> 각 줄에서 입력받으니까 x
    #S = input()
    new = ''
    for j in S:
        new += j*int(R)
    print(new)

#1157
S = input()
S = S.upper()
ch = list(set(S))
cnt = []
result = 0
for i in ch:
    cnt.append(S.count(i))
if cnt.count(max(cnt)) != 1:
    print('?')
else:
    result = ch[cnt.index(max(cnt))]
    print(result)

#1152
S = list(map(str, input().split()))
cnt = 0 #--> len(input().split())
for i in S:
    if i != ' ':
        cnt += 1
print(cnt)

#2908
a, b = input().split()
a = int("".join(reversed(a))) #a[::-1]
b = int("".join(reversed(b))) #b[::-1]
print(max(a, b))

#5622
a = input()
book = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
t = 0
for i in a:
    for j in book:
        if i in j:
            t += book.index(j) + 3
print(t)

#2941


#1316
