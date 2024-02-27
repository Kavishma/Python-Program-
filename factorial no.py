#factorial of given no

def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i=i+1
    print("factorial is ",fact)
n=int(input("enter a number:"))
factorial(n)
