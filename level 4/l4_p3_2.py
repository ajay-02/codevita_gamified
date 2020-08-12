k,n,t=list(map(int,input().split()))
l=[list(map(int,input().split())) for i in range(n)]
p=list(map(int,input().split()))
r=list(map(int,input().split()))
for i in range(n):
    x=0
    for j in range(n):
        l[i][j]=l[i][j]*int(p[x])
        x+=1
cnt=0
for i in range(n):
    v=int(p[i])
    w=v*int(r[i])
    for j in range(n):
        if(v>=k and w<=t):
            cnt+=1
            break
        w+=l[i][j]*int(r[j])
        v+=l[i][j]
print(cnt)