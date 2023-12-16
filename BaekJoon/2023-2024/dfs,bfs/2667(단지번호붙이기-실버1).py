#bfs 문제입니다

import sys
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(graph,a,b):
    n = len(graph)
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0 #재방문 막으려고
    count = 1 #여기서부터 넓이 시작임

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==1:
                    graph[nx][ny]=0#재방문 막기2
                    queue.append((nx,ny))
                    count+=1
            else:
                continue
    return count
cnt=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt.append(bfs(graph,i,j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])