#exchange the 2 variables
#temporary :

a=int(input("enter a:"))
b=int(input("enter b:"))
print("before swapping:",a,b)
c=a
a=b
b=c
print("after swapping:",a,b)

#without temporary:
a=int(input("enter a:"))
b=int(input("enter b:"))
print("before swapping:",a,b)
a=a+b
b=a-b
a=a-b
print("after swapping:",a,b)
