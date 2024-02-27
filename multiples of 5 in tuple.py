#find multiples of 5 in tuple

mytuple=(10,25,20,45,15,30,85)
mylist=[]
for i in mytuple:
    if (i%5==0 ):
        mylist.append(i)
print("multiple of 5 in tuple:\n",mylist)
