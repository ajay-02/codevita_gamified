string = str(input())
opn=['[','{',"("]
close=[']','}',')']
stack=[]
count=0
br=0
sc=0
f=0
ob=0
obs=0
for i in string:
    if i in opn:
        stack.append(i)
        br=br+1
        ob=1
        obs=0
    elif i=='*' and ob==1:
        sc=sc+1
        obs=obs+1
    elif i in close:
        pos = close.index(i)
        if (len(stack)>0) and (opn[pos] == stack[len(stack)-1]):
            stack.pop()
            if obs==0 or obs==1:
                br=br-1
                f=1
            if sc>=2:
                count = count + br
                sc=0
                ob=0
                br=0
            elif ob==1:
                f=1
        else:
            f=1
if len(stack)==0 and f==0 and count>0:
    print('Yes',count)
else:
    print('No',count)
