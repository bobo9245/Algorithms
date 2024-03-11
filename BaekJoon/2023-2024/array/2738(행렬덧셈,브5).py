n,m = map(int,input().split())
A = []
B = []
for i in range(n):
    list1 = list(map(int,input().split()))
    A.append(list1)
for i in range(n):
    list2 = list(map(int,input().split()))
    B.append(list2)
print(A)
print(B)
for i in range(n):
    for j in range(m):
        A[i][j] = A[i][j]+B[i][j]
for i in range(n):
    print(' '.join(map(str,A[i])))