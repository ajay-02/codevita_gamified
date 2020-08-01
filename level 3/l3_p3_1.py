t1,t2,m=map(int,input().split())
l=[]
if(t1>0 and t2>0 and m>0):
    for i in range(1,t2//2+1):
	a=i*((2*i)-1)
	for j in range(1,t2//2+1):
	    b=j*(j+1)//2
	    if((a==b) and (a>=t1 and a<=t2)):
		l.append(a)
    if(len(l)<m):
        print("No number is present at this index")
    else:
	print(l[m-1])
else:
    print("Invalid Input")
