score = ['A+','A0','B+','B0','C+','C0','D+','D0','F','P']

totalhj = 0.0
totalscore = 0.0



for i in range(20):
    gm,hj,rate = input().split()
    hj = float(hj)
    if rate==score[9]: continue
    elif rate==score[8]:
            totalhj = totalhj+hj
            continue
    for j in range(len(score)):        
        if rate==score[j]:
            totalhj = totalhj+hj
            totalscore = totalscore + hj*(4.5-(0.5*j))

print('%.6f' %(totalscore/totalhj))