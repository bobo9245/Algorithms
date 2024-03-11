n = int(input())

dohwaji = [[0]*100 for _ in range(100)]

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            dohwaji[x+i-1][y+j-1] = 1

ans=0
for i in range(100):
    for j in range(100):
        if dohwaji[i][j]==1:
            ans = ans+1

print(ans)