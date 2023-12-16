import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)


for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

count=0
for i in range(1,n+1):
    if not visited[i]:
        count+=1
        DFS(i)
print(count)