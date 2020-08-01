s=input()
l=[]
flag=0
count=0
for i in range(len(s)):
    if(s[i]=='{' or s[i]=='[' or s[i]=='('):
        l.append(s[i])
        flag=1
    if(len(l)>0):
        if(s[i]=='}'):
            if(l[-1]=='{'):
                l.pop()
                continue
            else:
                break
        if(s[i]==']'):
            if(l[-1]=='['):
                l.pop()
                continue
            else:
                break
        if(s[i]==')'):
            if(l[-1]=='('):
                l.pop()
                continue
            else:
                break
        if(s[i]=='*'):
            if(s[i+1]=='*'):
                if(l[-1]=='(' or l[-1]=='{' or l[-1]=='['):
                    count=count+1
    else:
        if(flag==1):
            flag=0
            break
if(len(l)==0 and flag==1):
    print('Yes',count)
else:
    print('No',count)

