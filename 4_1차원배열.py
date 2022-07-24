#10818
a = int(input())
A = list(map(int, input().split()))
print(min(A), max(A))

#2562
A = []
for _ in range(9):
    a = int(input())
    A.append(a)
print(max(A))
print(A.index(max(A)) + 1)

#2577
a = int(input())
b = int(input())
c = int(input())
A = list(str(a*b*c))
for i in range(10):
    print(A.count(str(i)))

#3052
A = []
for _ in range(10):
    a = int(input())
    A.append(a%42)
A = set(A)
print(len(A))

#1546
N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    B.append(A[i]/max(A) *100)
print(sum(B)/N)

#4344
C = int(input())
for _ in range(C):
    A = list(map(int, input().split()))
    avg = sum(A[1:])/A[0]
    cnt = 0
    for i in A[1:]:
        if i > avg:
            cnt += 1
    result = cnt/A[0] * 100
    print(f'{result:.3f}%')
