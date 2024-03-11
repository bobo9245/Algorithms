# print(ord('0'))

numbers = ['0','1','2','3','4','5','6','7','8','9']

list0, num = input().split()
list1 = list(list0)
num1 = int(num)
list1.reverse()
for i in range(len(list1)):
    if list1[i] in numbers:
        list1[i] = int(list1[i])
    else:
        list1[i] = ord(list1[i])
        list1[i] = list1[i]-55

ans = 0
for i in range (len(list1)):
    ans = ans + list1[i] * (num1**i)

print(ans)