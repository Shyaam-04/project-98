import random
choice = 0
numberToGuess = random.randint(1,9)


while choice<=5 :
    inputNumber = int(input("Enter a number from 1 to 9: "))
    if(inputNumber == numberToGuess):
        print("You found the number. Congragulations!")
        break
    elif(inputNumber< numberToGuess):
        print("Try a number greater ")
        choice = choice+1
    else:
        print("Try a number lesser ")
        choice = choice+1

if(choice >= 5):
    print("YOU LOSE!!")
    




