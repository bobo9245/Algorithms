def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    less=[]
    more=[]
    equal=[]
    for num in arr:
        if(num<pivot):
            less.append(num)
        elif num==pivot:
            equal.append(num)
        else:
            more.append(num)

    return quicksort(less)+equal+quicksort(more)
