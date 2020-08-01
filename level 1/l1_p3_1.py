min1=10**9
cnt=0
def permutation(s,i,n,p): 
    global min1,cnt
    if(i==n): 
        q=int(''.join(s))
        if(q-p>0 and q<min1): 
            min1=q
            cnt=1
    else:
        for j in range(i,n+1):
            s[i],s[j]=s[j],s[i]
            permutation(s,i+1,n,p)
            s[i],s[j]=s[j],s[i]
    return min1
a=input()
b=int(input())
s=list(a)
le=len(s)
per=permutation(s,0,le-1,b)
if cnt==1:
    print(per)
else: 
    print(-1)
