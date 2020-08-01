b,n=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    b-=(i%2)+(i//2)
    print(b)
if(b<0):
    print("NO")
else:
    print("YES")
