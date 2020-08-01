for _ in range(int(input())):
    s=input()
    x=list(input())
    for i in s:
        if(i in x):
            print(i,end='')
            x.remove(i)
        if(len(x)==0):
            break
    print()
