n=int(input())
p=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j or j+i==n+1):
            print(p,end=" ")
        else:
            print(" ",end='')
    p-=1
    print()