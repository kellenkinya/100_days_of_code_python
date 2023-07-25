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