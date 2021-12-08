import random

print("Number Guessing Game-->")
x=random.randint(1,10)

chances=0

while chances < 5:
    guess=int(input('Enter your Guess: '))
   
    if guess == x:
       print("CONGRATULATION YOU HAVE WON!!!")
       break
    elif guess<x:
        print("Your Guess was too low: Guess a number higher than ", guess)
    else: 
        print("Your Guess was too high: Guess a number lower than ", guess)
    chances+=1

if not chances < 5:
    print("You LOSE!! Better Luck Next Time. The number was ", x)
    




