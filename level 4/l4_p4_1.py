def gcd(a,b):
    return a if(b==0) else gcd(b,a%b)
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    i,ans,c=0,1,0
    while(i<=n-1):
        temp_i=i
        c=0
        while(a[i]!=0):
            temp=i
            i=a[i]-1
            a[temp]=0
            c+=1
        i=temp_i+1
        if(c!=0):
            ans=ans*c//gcd(ans,c)
    print(ans)
