def gcd(a,b):
    return a if(b==0) else return gcd(b,a%b)
def solve(l,p):
    if(gcd(l,p)!=1):
        return -1
    res=1
    k=1
    while(k<n):
        res=(res*l)%n
        if(res==1):
            return k
        k+=1
    return -1
l,p=int(input()),int(input())
print(solve(l,p)) 