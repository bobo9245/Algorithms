arr1 = [1,2,3]
num1 = 5
arr1.append(num1)
print('\n\n')
print('arr1.append(num1):',arr1)


arr1 = [1,2,3]
arr2 = [4,5,6]
arr1.append(arr2)
print('\n\n')
print('arr1.append(arr2):',arr1)


arr1 = [1,2,3]
arr2 = [4,5,6]
arr1.extend(arr2)
print('\n\n')
print('arr1.extend(arr2):',arr1)


arr1 = [1,2,3]
arr3 = [1,2,[3,4,5,[6]]]
arr1.extend(arr3)
print('\n\n')
print('arr1.extend(arr3):',arr1)
print('\n\n')
print('\n\n')