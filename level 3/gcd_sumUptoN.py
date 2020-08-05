def gcd(a,b):
    return a if(b==0) else gcd(b,a%b)
n=int(input())
s=0
for i in range(1,n):
    for j in range(i+1,n+1):
        s+=gcd(i,j)
print(s)
