#min list

mylist=[3,25,8,9]
i=1
min=mylist[0]
while(i<4):
    if(mylist[i]<min):
        min=mylist[i]
    else:
        i=i+1
print("minimum",min)
