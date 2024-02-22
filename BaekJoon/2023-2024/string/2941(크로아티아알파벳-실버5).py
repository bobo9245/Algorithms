import re

str = input()

ans = len(str)
ans = ans-len(re.findall(r'c=',str))
ans = ans-len(re.findall(r'c-',str))
ans = ans-len(re.findall(r'dz=',str))
ans = ans-len(re.findall(r'd-',str))
ans = ans-len(re.findall(r'lj',str))
ans = ans-len(re.findall(r'nj',str))
ans = ans-len(re.findall(r's=',str))
ans = ans-len(re.findall(r'z=',str))





print(ans)

