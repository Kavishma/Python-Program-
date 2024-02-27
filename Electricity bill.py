#Electricity bill
u = int(input("enter a units:"))
if (u==100):
    fc=0
    ec=0
    ap=fc+ec
elif (u<=200):
    fc=20
    ec=(u-100)*1.5
    ap=fc+ec
elif(u<=500):
    fc=20
    ec=(u-200)*3+(100*2)
    ap=fc+ec
else :
    fc=20
    ec=(u-500)*6.6+(300*4.6)+(100*3.5)
    ap=fc+ec
print("Total Amount Paid",ap)
