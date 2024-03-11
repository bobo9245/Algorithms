import sys
import collections
n =  int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int,sys.stdin.readline().split())))

max=0
for i in matrix:
    for j in i:
        if max<j:
            max = j

dx,dy = [-1,1,0,0],[0,0,-1,1]

def bfs(x,y,h,visited):
    queue = collections.deque([])
    queue.append([x,y])
    visited[x][y]=1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if matrix[nx][ny]>h and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    queue.append([nx,ny])

                
ans=0
for i in range(max):
    visited = [[0]* n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if matrix[j][k]>i and visited[j][k]==0:
                bfs(j,k,i,visited)
                cnt+=1

    if ans<cnt:
        ans=cnt
print(ans)
