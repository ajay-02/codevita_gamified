'''

input:
3

output:
10203010011012
**4050809
****607

'''

n=int(input())
left_tri=1
right_tri=(n*n)+1
i=n
while(i>0):
    print('**'*(n-i),end='')
    for j in range(1,i+1):
        print(left_tri,end='0')
        left_tri+=1
    for j in range(1,i+1):
        print(right_tri,end='')
        if(j<i):
            print('0',end='')
        right_tri+=1
    i-=1
    right_tri=right_tri-(i*2)-1
    print()
