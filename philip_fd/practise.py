import random
from enum import IntEnum


class Action(IntEnum):
    Rock=0
    Paper=1
    Scissors=2

def user_selection():
    choice= [f"{action.name}[{action.value}] " for action in Action]
    choices_str= ",".join(choice)
    selection= int(input(f"Please choose among {choices_str}: "))
    action= Action(selection)
    return action



def computer_selection():
    selection= random.choice(0,len(Action)-1)
    action=Action(selection)
    return action

def determine_winner(user,computer):
    win= {
        Action.Paper: [Action.Rock],
        Action.Rock:[Action.Scissors],
        Action.Scissors:[Action.Paper]
    }

    defeat= win[user]


    if user==computer:
        print(f"You both chose{user} its a tie")
    elif  computer in defeat:
        print("you win")
    else:
        print("you lose")

def play_again():
    while True:
        try:
            user=user_selection
        except ValueError as e :
            right_selection=f"[0, {len(Action)-1}"
            print(f" choose the correct {right_selection}")
            continue
        computer=computer_selection
        determine_winner(user,computer)

        feedback=input("Do u you want to play again")
        if feedback.lower()!="y":
            break


play_again()


####################hangman project###3
from words import words
import string


def  get_valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word= random.choice(words)
    return word.upper()


def hangman():
    word= get_valid_words(words)
    word_string=set(word)
    alphabet=string.ascii_uppercase
    used_letters=set()


    lives=7

    while lives>0 and len(word_string)>0:
        print("you have ", lives, "you have used these letter ", " ".join(used_letters))

        #get the current word filling which letter have been guessed and those not guessed

        letters_in_word_string=[letters if letters in used_letters else "-" for letters in word]

        print(" This is the word so far: ", " ".join(letters_in_word_string))

        user_letters= input("please guess your letter").upper()

        if user_letters in alphabet-used_letters:
            used_letters.add(user_letters)
            if user_letters in word_string:
                word_string.remove(user_letters)
            else:
                lives=lives-1
                print("letter not in word")
        elif  user_letters in used_letters:
            print("you have used : this letter")
        else:
            print("please guess a correct letter")

        
        if lives==0:
            print("you are out of lives")
        else:
            print("you got the correct word")


hangman()