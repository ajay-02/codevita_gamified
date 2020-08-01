a,b=int(input()),int(input())
l=[0]*(a-1)
l.append(1)
while(len(l)<b):
    l.append(sum(l[-a:]))
print(*l)
