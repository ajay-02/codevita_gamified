def solve(n):
    s=0
    while(n>0):
        s+=n%6
        n//=6
    return s
n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    l[i]=solve(l[i])
cnt=0
for i in range(0,n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            cnt+=1
print(cnt)
