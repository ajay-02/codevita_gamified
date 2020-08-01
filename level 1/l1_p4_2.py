from itertools import permutations
def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True
n,cnt=int(input()),0
l=[str(i) for i in range(2,n+1) if(prime(i))]
l=list(permutations(l,2))
for i in l:
    if(prime(int(''.join(i)))):
        cnt+=1
print(cnt)
