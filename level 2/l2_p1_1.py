n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
maxi,mini=0,0
for i in range(n):
    prod=a[i]*b[i]
    if(prod<0 and b[i]<0):
        t=(a[i]+2*k)*b[i]
    elif(prod<0 and a[i]<0):
        t=(a[i]-2*k)*b[i]
    elif(prod>0 and a[i]<0):
        t=(a[i]+2*k)*b[i]
    elif(prod>0 and a[i]>0):
        t=(a[i]-2*k)*b[i]
    d=abs(prod-t)
    if(d>maxi):
        maxi=d
    mini+=prod 
print(mini-maxi)
