p,r,t=input().split()
p=int(p)
r=int(r)
t=int(t)
CI=p*pow((1+r/100),t)
print("%.2f"%CI)