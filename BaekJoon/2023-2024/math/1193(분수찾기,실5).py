X=int(input())

num=1
if X==1:
    print('1/1')
for i in range(1,4473,1):
    num = num+i
    if X<num:
        print(str(num-X)+'/'+str((i+1)-(num-X)))
        break