n=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s^=i
print('JASBIR') if(s==0) else print('AMAN')