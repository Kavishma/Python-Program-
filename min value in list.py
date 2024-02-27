#find min value in list

mylist=[25,11,3,8,16,1]
min=mylist[0]
for i in mylist:
    if i<min:
        min=i
print("min value in list\n",mylist)
print(min)
