#12865
N, K = map(int, input().split())
dp = [[0] * (K+1) for i in range(N+1)]
li = [[0, 0]]
for i in range(N):
    w, v = map(int, input().split())
    li.append([w, v])
for i in range(1, N+1):
    w = li[i][0]
    v = li[i][1]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
print(dp[N][K]) 

#11060
N = int(input())
a = list(map(int, input().split()))
dp = [N + 1] * N
dp[0] = 0
for i in range(N):
    for j in range(1, a[i] + 1):
        if i+j < N:
            dp[i+j] = min(dp[i+j], dp[i] + 1)
if dp[N-1] == N + 1:
    print(-1)
else:
    print(dp[N-1])
