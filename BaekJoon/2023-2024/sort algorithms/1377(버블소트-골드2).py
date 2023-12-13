import sys
input = sys.stdin.readline

N = int(input())
arr=[]

for i in range(N):
    arr.append((int(input()),i))

max = 0
sorted_arr = sorted(arr)

for i in range(N):
    if max<sorted_arr[i][1] - i:
        max = sorted_arr[i][1]-i

print(max+1)