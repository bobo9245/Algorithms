n = int(input())
x,y = map(int,input().split())
matrix = [[]for _ in range(n+1)]

m = int(input())
for i in range(m):
    x1,y1 = map(int,input().split())
    matrix[x1].append(y1)
    matrix[y1].append(x1)

print(matrix)