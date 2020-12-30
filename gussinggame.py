import random 
chances=0
print("number gussing game")
number=random.randint(1,9)
print("guess the numver between 1 and 9")
while(chances<5):
    guess=int(input("enter you'r guess"))
    if(guess==number):
        print("Congratulations you WON")
        break
    elif(guess<number):
        print("You'r guess was too low guess a higher number")
    else:
        print("you'r guess was too high guess a low number")
    chances=chances+1
if(chances>=5):
    print("you lost the game")
        