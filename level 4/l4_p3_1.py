for i in range(int(input())):
    t,p=map(int,input().split())
    if(t>=p):
        print(1)
    else:
        pa=p//t
        pb=pa+1
        tb=p%t
        ta=t-tb
        fact=list((1,1))
        for i in range(2,p+2):
            fact.append(i*fact[i-1])
        div=fact[p]//((fact[pa]**ta)*(fact[pb]**tb)*fact[ta]*fact[tb])
        if pb>=4:
            x=int(div*(fact[pa-1])**ta*(fact[pb-1])**tb)
        else:
            x=div
        print(x)