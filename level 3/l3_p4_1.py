def is_prime(n):
    if(n>1):
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        return True
    return False
n=int(input())
count=0
arr=[i for i in range(2,n+2) if(is_prime(i))]
s=arr[0]
for i in range(1,len(arr)):
    s=s+arr[i]
    if s<=n:
        if is_prime(s):
            count=count+1
print(count)
