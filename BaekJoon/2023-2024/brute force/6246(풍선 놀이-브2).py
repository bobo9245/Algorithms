n,q = map(int,input().split())

array = [False]*n

for i in range(q):
    a,b = map(int,input().split())
    for j in range(a-1,n,b):
        array[j]=True

count=0
for n in array:
    if n==False:
        count+=1

print(count)