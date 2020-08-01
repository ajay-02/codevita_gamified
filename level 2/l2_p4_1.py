s=input()
n=s
x=''
for i in range(int(input())):
    ls=input().split()
    r=int(ls[1])
    if(ls[0]=='R'):
        s=s[len(s)-r:]+s[:len(s)-r]
    elif(ls[0]=='L'):
        s=s[r:]+s[:r]
    x+=s[0]
x=sorted(x)
l=len(x)
flag=0
for i in range(0,len(n)-l+1):
    if(sorted(n[i:l+i])==x):
        flag=1
        break
print('Yes') if(flag==1) else print('No')
