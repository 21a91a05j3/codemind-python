n=int(input())
m=int(input())
for i in range(n,m+1):
    t=i
    s=0
    while(t):
        d=t%10
        t=t//10
        s=s*10+d
    if(s==i):
        print(i,end=' ')