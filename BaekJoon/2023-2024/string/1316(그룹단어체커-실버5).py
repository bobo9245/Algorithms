n = int(input())
ans = 0

for i in range(n):
    strlist = list(input())
    if len(strlist)==1:
        ans = ans+1
        continue
    isgroup=True
    checklist = []
    for j in range(len(strlist)):
        if j==0:
            checklist.append(strlist[j])
        elif strlist[j] in checklist:
            if strlist[j-1]==strlist[j]:
                continue
            else:
                isgroup=False
                break
        else:
            checklist.append(strlist[j])
    if isgroup:
        ans = ans+1
    

print(ans)
