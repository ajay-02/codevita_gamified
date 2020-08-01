p=float(input())
y=int(input())
b=[]
l=0
for k in range(2):
    n=int(input())
    sum=0
    for _ in range(n):
        yrs,s=input().split()
        yrs=int(yrs)
        s=float(s)
        sq=((1+s)**(yrs*12))
        emi=p*(s/(1-1/sq))
        sum+=emi
    b.append(sum)
print('Bank A') if(b[0]<b[1]) else print("Bank B")
