n = int(input())

for i in range(n):
    arr = [0]*4
    num = int(input())
    
    if num>=25:
        arr[0] = num//25
    num = num-arr[0]*25
    if num>=10:
        arr[1] = num//10
    num = num-arr[1]*10
    if num>=5:
        arr[2] = num//5
    num = num-arr[2]*5
    arr[3] = num

    print(' '.join(map(str,arr)))