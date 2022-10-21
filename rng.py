from operator import truediv
import random
randomtall = random.randint(1,10)

numberofguesses = 1

isrunning = True 

guess = int( input("Gjett på et tall mellom 1 og 10 ") )
 

while (isrunning):
   
    if (numberofguesses < 3):
        if (guess == randomtall):
            print("Du gjettet riktig")

            isrunning = False
        elif (guess < randomtall):
            (numberofguesses + 1) 
            print("Du gjettet for lavt")
            guess = int (input("Gjett igjen "))

        elif (guess > randomtall):
            (numberofguesses + 1) 
            print("Du gjettet for høyt")
            guess = int (input("Gjett igjen "))


    else:
         print("Du har gjettet feil for mange ganger")
         print("Game over")
         isrunning = False
    