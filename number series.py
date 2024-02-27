#number series

x=int(input("enter x:"))
n=int(input("enter n:"))
s=0
i=0
while(i<=n):
    s=s+x**i
    i=i+1
print("sum of series",s)
