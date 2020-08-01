n=int(input())
s=2
if(n>2):
    if(n==3):
        print(s)
    else:
        for i in range(1,n-2):
            s=((s*2)+2)%10000000007
        print(s)
else:
    print(0);
