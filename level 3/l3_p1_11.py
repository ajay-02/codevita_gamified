def fib(n):
    l=[1,0,1]
    for i in range(3,n+1):
        l.append(((i-1)*(l[i-1]+l[i-2]))%100000007)
    return l[n]
n=int(input())
print(fib(n))
