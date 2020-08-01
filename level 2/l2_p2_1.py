for _ in range(int(input())):
    s=list(input())
    se=list(set(s))
    flag=0
    for i in se:
        if (ord(i)-96)!=s.count(i):
            flag=1
            break
    if(flag):
        print('NO',end=' ')
    else:
        print('YES',end=' ')
