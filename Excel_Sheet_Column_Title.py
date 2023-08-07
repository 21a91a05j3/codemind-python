n=int(input())
a='ABCDEFGHIJKLMNopQRSTUVWXYZ'
r,l=n-1,''
while(r>=0):
    l=a[r%26]+l
    r=(r//26)-1
print(l)