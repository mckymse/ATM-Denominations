from itertools import count
from pprint import pprint
from operator import itemgetter

n=int(input())
amt=int(input())
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
perm=[]
l=num1
m=num2
n=num3
o=num4
perm.append({1000:0,500: 0, 200: 0, 100: 0})
if n< 100:
    for num4 in count(0):
        for num3 in count(0):
          for num2 in count(0):
            for num1 in count(0):
              if num1 * 100 + num2 * 200 + num3 * 500 + num4 * 1000== amt and num1<=l and num2<=m and num3 <=n and num4<=o and ((num1+num2+num3+num4)<=10):
                            
                  perm.append({1000:num4,500: num3, 200: num2, 100: num1})
                  num1-=1
                  num2-=1
                  num3-=1
                  num4-=1
              
              if num1 * 100 + num2 * 200 + num3 * 500 + num4 * 1000 > amt:
                break
            if num2 * 200 + num3 * 500 + num4 * 1000 > amt:
              break
          if num3 * 500 + num4 * 1000 > amt:
            break
        if num4 * 1000 > amt:
           break

perm.sort(key = itemgetter(100))
perm.sort(key = itemgetter(200), reverse = True)
perm.sort(key = itemgetter(500), reverse = True)
perm.sort(key = itemgetter(1000), reverse = True)

max=0
for i in range(len(perm)):
    
        
        a=perm[i][100]
        b=perm[i][200]
        c=perm[i][500]
        d=perm[i][1000]
        e=a+b+c+d
        
        if(e>max):
            max=e
if(max>0):
    print(max)
else:
    print('0')









