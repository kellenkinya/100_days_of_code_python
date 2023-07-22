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
#guess(10)

def modified_guess(start_number,end_number):
    start_number=int(input("write your start  number "))
    end_number=int(input("write your end  number "))
    random_number= random.randint(start_number,end_number)
    guess_number= 0

    while random_number!=guess_number:
        guess_number=int(input(f"guess a number between {start_number} and {end_number}: "))

        if guess_number>random_number:
            print(f"The guess number: {guess_number} is too high")
            end_number=guess_number
            print(end_number)
        elif guess_number<random_number:
            print(f"The guess number: {guess_number} is too low")
            start_number=guess_number
            print(start_number)
    print(f"You are correct, the number is {guess_number}")

#modified_guess(1,10)

def computer_guess(x):
    low=1
    high=x
    feedback=''

    while feedback !='c':
        if low!=high:
            guess_number=random.randint(low, high)
        else:
            guess_number=low
        
        

        feedback=input(f"Did the computer correct the right number {guess_number}. if guess is too high print(H) if guess is low type (L)".lower())

        
        if feedback=='h':
            high=guess_number-1
        elif feedback=='l':
            low=guess_number+1
        
    print(f" comouter guess {guess_number} correct")


computer_guess(10)

        