n=int(input())
a=list(map(int,input().split()))
p=1
for i in a:
    p*=i
for i in a:
    print(p//i,end=' ')