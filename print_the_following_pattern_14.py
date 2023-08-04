n=int(input())
for i in range(1,n+1):
    for j in range(n-i,0,-1):
        print(" ",end='')
    for j in range(1,n+1):
        if(i==1 or i==n):
            print("*",end='')
        else:
            if(j==1 or j==n):
                print("*",end='')
            else:
                print(" ",end='')
    print()