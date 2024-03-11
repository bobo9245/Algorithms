arr=[]
for i in range(5):
    arr.append(list(input()))

lenarr = [len(arr[0]),len(arr[1]),len(arr[2]),len(arr[3]),len(arr[4])]
ans = ''
for i in range(max(lenarr)):
    for j in range(5):
        if i<lenarr[j]:
            ans = ans+(arr[j][i])
print(ans)