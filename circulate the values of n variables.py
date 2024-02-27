#circulate the values of n variables

def circulate(listt,num_of_rotation):
    i=1
    while (i<=num_of_rotation):
        j=len(listt)-1
        while(j>0):
            temp=listt[j]
            listt[j]=listt[j-1]
            listt[j-1]=temp
            j=j-1
        print("rotation",i,listt)
        i=i+1
    return
listt=[1,2,3,4,5]
circulate(listt,5)
