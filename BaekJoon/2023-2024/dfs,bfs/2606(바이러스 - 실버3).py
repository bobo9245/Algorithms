import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

#컴퓨터개수
n = int(input())
visited = [False] * (n+1)
#간선개수
m = int(input())

#[1]부터 [n]까지 활용할거임
graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(1)
print(visited.count(True)-1) #본인은 빼야함