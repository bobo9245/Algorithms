import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
arrive = 0

n,m = map(int,input().split())
visited = [False] * n
con = [[] for _ in range(n)]

for i in range(m):
    s,e = map(int,input().split())
    con[s].append(e)
    con[e].append(s)


def dfs(v,depth):
    global arrive
    if depth ==5:
        arrive=1
        return 0
    visited[v] = True
    for i in con[v]:
        if not visited[i]: #이 줄을 통해 node가 겹치는걸 방지해줌.
            dfs(i,depth+1)
    visited[v]=False

for i in range(n):
    dfs(i,1)
    if arrive:
        break

print(arrive)