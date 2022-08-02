#2798
N, M = map(int, input().split())
card = list(map(int, input().split()))
sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if card[i] + card[j] + card[k] > M:
                continue
            else: #저장하면서 더 큰 값으로 업데이트
                sum = max(sum, card[i] + card[j] + card[k])
print(sum)

#2231
N = int(input())
result = 0
for i in range(1, N+1):
    d = sum(list(map(int, str(i))))
    result = i + d
    if result == N:
        print(i)
        break
    if i == N:
        print(0)

#7568
N = int(input())
li = []
for _ in range(N):
    x, y = map(int, input().split())
    li.append((x, y))
for i in li:
    rank = 1
    for j in li:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank)

#1018
N, M = map(int, input().split())
cnt = []
board = []
for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        cnt1 = 0
        cnt2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'W':
                        cnt1 += 1
                    if board[k][l] != 'B':
                        cnt2 += 1
                else:
                    if board[k][l] != 'B':
                        cnt1 += 1
                    if board[k][l] != 'W':
                        cnt2 += 1
        cnt.append(min(cnt1, cnt2))
print(min(cnt))

#1436
