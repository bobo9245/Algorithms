import sys
from collections import deque

m, n, h = map(int, input().split())
matrix = []
queue = deque([])

#순서대로 z,y,x
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if(temp[j][k]==1):
                queue.append([i,j,k])
    matrix.append(temp)

dx, dy,dz = [-1, 1, 0, 0,0,0], [0, 0, -1, 1,0,0],[0,0,0,0,-1,1]

while queue:
    x,y,z = queue.popleft()
    for i in range(6):
        nx,ny,nz = x+dx[i],y+dy[i],z+dz[i]
        if 0<=nx<h and 0<=ny<n and 0<=nz<m and matrix[nx][ny][nz]==0:
            queue.append([nx,ny,nz])
            matrix[nx][ny][nz]=matrix[x][y][z]+1
                

day = 0
for i in matrix:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)