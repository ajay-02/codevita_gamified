def burnt_time(l,cr,cc,r,c,f_time,time):
    if((cr>=r) or (cr<0) or (cc>=c) or (cc<0) or (l[cr][cc]=='W')):
        return
    if((f_time[cr][cc]!=-1) and (time>=f_time[cr][cc])):
        return
    f_time[cr][cc]=time
    burnt_time(l,cr+1,cc+1,r,c,f_time,time+1)
    burnt_time(l,cr+1,cc,r,c,f_time,time+1)
    burnt_time(l,cr+1,cc-1,r,c,f_time,time+1)
    burnt_time(l,cr,cc+1,r,c,f_time,time+1)
    burnt_time(l,cr,cc-1,r,c,f_time,time+1)
    burnt_time(l,cr-1,cc+1,r,c,f_time,time+1)
    burnt_time(l,cr-1,cc,r,c,f_time,time+1)
    burnt_time(l,cr-1,cc-1,r,c,f_time,time+1)
r,c=map(int,input().split())
x,y=map(int,input().split())
l=[]
for i in range(0,r):
    l.append(list(input().split()))
f_time=[[-1]*r for i in range(c)]
time=1
burnt_time(l,x-1,y-1,r,c,f_time,1)
max=0
for i in range(0,r):
    for j in range(0,c):
        if(f_time[i][j]>max):
            max=f_time[i][j]
print(max)