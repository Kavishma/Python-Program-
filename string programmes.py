#string palindrome

n=input("enter a string:")
if (n==n[::-1]):
    print("palindrome")
else:
    print("not palindrome")


#count vowels

n=input("enter string:")
vowels =0
for i in n:
    if i in ("a","e","i","o","u","A","E","I","O","U"):
        vowels=vowels+1
print("no of vowels:",vowels)

#char from str

n=input("enter a string:")
char=input("enter delete str:")
mylist=[]
for i in n:
    if(i==char):
        continue
    else:
        mylist.append(i)
print(''.join(mylist))
    
