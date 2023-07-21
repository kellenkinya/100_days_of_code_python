#make a function
#import random
# use two variable the guess number and random number generatd by the pc
#use if to show high and low
#create a while loop to be tfalase until true


import random

def guess(x):
    random_number= random.randint(1,x)
    guess_number= 0

    while random_number!=guess_number:
        guess_number=int(input(f"guess a number between 1 and {x} "))

        if guess_number>random_number:
            print(f"The guess number: {guess_number} is too high")
        elif guess_number<random_number:
            print(f"The guess number: {guess_number} is too low")
        
    print(f"You are correct, the number is {guess_number}")
guess(10)

def modified_guess(x):
    start_number=int(input("write your start  number "))
    end_number=int(input("write your end  number "))
    random_number= random.randint(start_number,end_number)
    guess_number= 0

    while random_number!=guess_number:
        guess_number=int(input(f"guess a number between 1 and {x}: "))

        if guess_number>random_number:
            print(f"The guess number: {guess_number} is too high")
            
        elif guess_number<random_number:
            print(f"The guess number: {guess_number} is too low")
        