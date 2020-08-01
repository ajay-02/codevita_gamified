from itertools import combinations
x=input()
n=list(x)
l=len(n)
res=0
while(True):
    c=[int(''.join(list(i))) for i in list(combinations(n,l))]
    for i in c:
        if(i%8==0):
            res=1
            break
    if(res==1 or l==1):
        break
    l-=1
if(res==1):
    print(x,'Yes')
else:
    print(x,'No')
