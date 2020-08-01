n,k=map(int,input().split())
l=[]
for i in range(1,n//2+1):
    if(n%i==0):
        l.append(i)
l.append(n)
if(len(l)<k):
    print(1)
else:
    print(l[-k])
