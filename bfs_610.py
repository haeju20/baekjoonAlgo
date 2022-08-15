#1697
from collections import deque
import sys
S = int(sys.stdin.readline())
q = deque()
q.append((1, 0))
emo = [[-1] * (S+1) for _ in range(S+1)]
emo[1][0] = 0
result = -1
while q:
    s, c = q.popleft()
    if emo[s][s] == -1:
        emo[s][s] = emo[s][c] + 1
        q.append((s, s))
    if s+c <= S and emo[s+c][c] == -1:
        emo[s+c][c] = emo[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and emo[s-1][c] == -1:
        emo[s-1][c] = emo[s][c] + 1
        q.append((s-1, c))
for i in range(S+1):
    if emo[S][i] != -1:
        if result == -1 or result > emo[S][i]:
            result = emo[S][i]
print(result)    

#13913


#14226


#13549


#1261
