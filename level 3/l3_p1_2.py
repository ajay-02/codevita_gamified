b,n=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in l:
    b-=(i%2)+(i//2)
print("NO") if(b<0) else print("YES")
