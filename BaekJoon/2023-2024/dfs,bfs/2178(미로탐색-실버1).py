from collections import deque

n,m = map(int, input().split())
matrix = [list(map(int,input())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue.append([0,0])

def dfs():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and matrix[nx][ny]==1:
                matrix[nx][ny]=matrix[x][y]+1
                queue.append([nx,ny])

dfs()

print(matrix[n-1][m-1])