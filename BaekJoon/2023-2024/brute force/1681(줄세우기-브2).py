n,m = map(int,input().split())

ans = 0

while n:
    ans +=1
    arr = str(ans).split()
    print(arr)
    if str[m] not in arr:
        n -=1

print(ans)