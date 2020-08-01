from itertools import permutations 
n,d=map(int,input().split())
cnt=0
digit_arr=list(str(n))
digit_arr.sort()
p=permutations(digit_arr)
flag=0
m=-1
for i in list(p):
    num=int(''.join(i))
    if(num%d==0):
        if(num<m or m==-1):
            m=num
            flag=1
            print(num)
            break
if(flag!=1):
    print(-1)
