array = []
for i in range(9):
    array.append(list(map(int,input().split())))


x = 0
y=0
max=0

for i in range(9):
    for j in range(9):
        if array[i][j]>=max:
            max=array[i][j]
            x=i+1
            y=j+1

print(max)
print(str(x)+' '+str(y))