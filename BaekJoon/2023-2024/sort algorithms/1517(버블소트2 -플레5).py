def merge_sort(arr, temp, left, right):
    swaps = 0

    if left < right:
        mid = (left + right) // 2

        swaps += merge_sort(arr, temp, left, mid)
        swaps += merge_sort(arr, temp, mid + 1, right)
        swaps += merge(arr, temp, left, mid, right)

    return swaps

def merge(arr, temp, left, mid, right):
    swaps = 0

    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
            swaps += (mid - i + 1)  # 스왑 횟수 계산
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return swaps

# 입력 받기
n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n

# 병합 정렬을 사용한 스왑 횟수 계산
swaps = merge_sort(arr, temp, 0, n - 1)
print(swaps)
