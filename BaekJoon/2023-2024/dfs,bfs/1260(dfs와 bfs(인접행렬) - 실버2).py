from collections import deque

def dfs(matrix,i,visited):
    visited[i]=True
    print(i,end=' ')
    for j in range(1,n+1):
        if visited[j]==False and matrix[i][j]==1:
            dfs(matrix,j,visited)

def bfs(matrix,i,visited):
    queue=deque([i])
    visited[i]=True
    while queue:
        value = queue.popleft()
        print(value,end=' ')
        for j in range(1,n+1):
            if visited[j]==False and matrix[i][j]==1:
                queue.append(j)
                visited[j]=True

n,m,v = map(int,input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b]=1
    matrix[b][a]=1

visited=[False]*(n+1)
dfs(matrix,v,visited)
print()
visited=[False]*(n+1)
bfs(matrix,v,visited)
