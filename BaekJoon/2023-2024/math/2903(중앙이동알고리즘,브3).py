n = int(input())


addnum = 0
for i in range(n):
    addnum = addnum+(2**i)
print((2+(addnum))**2)