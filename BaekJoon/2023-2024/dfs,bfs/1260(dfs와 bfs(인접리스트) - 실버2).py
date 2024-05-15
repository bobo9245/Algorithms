from collections import deque

def dfs(matrix,i,visited):
    visited[i]=True
    print(i,end=' ')
    for j in matrix[i]:
        if not visited[j]:
            dfs(matrix,j,visited)

def bfs(matrix,i,visited):
    queue=deque([])
    queue.append(i)
    visited[i]=True
    while queue:
        value = queue.popleft()
        print(value,end=' ')
        for n in matrix[value]:
            if not visited[n]:
                queue.append(n)
                visited[n]=True

n,m,v = map(int,input().split())
matrix = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a].append(b)
    matrix[b].append(a)
for i in matrix:
    i.sort()

visited=[False]*(n+1)
dfs(matrix,v,visited)
print()
visited=[False]*(n+1)
bfs(matrix,v,visited)
