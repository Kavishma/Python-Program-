#guees the number

n = int(input("enter n : "))
i=0
attempt=3
while(i<attempt):
    guess=25
    if(n==guess):
        print("good job")
        break
    else:
        if(n>guess):
            print("your guess is high")
        else:
            print("your guess is low")
    break

