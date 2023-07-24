import random


    
def play():
    user=input("What is your choice r or s or p? ")
    computer= random.choice(['r','s','p'])

    if user==computer:
        return 'its a tie'
    
    if is_win(user, computer):
        return 'you won'
    
    return 'you lost'

def is_win(player, opponent):
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p'and opponent=='r'):
        return True

print(play())




from enum import IntEnum


class Action(IntEnum):
    Rock=0
    paper=1
    scissors=2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

def determine_winners(user_action, computer_action):
    if (user_action==Action.Rock and computer_action==Action.scissors) or (user_action==Action.scissors and computer_action==Action.paper) or(user_action==Action.paper and computer_action==Action.Rock):
        print(f"You win ")
    elif (user_action==Action.Rock and computer_action==Action.paper) or (user_action==Action.scissors and computer_action==Action.Rock) or (user_action==Action.paper and computer_action==Action.scissors):
        print(f"You lose")
    elif user_action==computer_action:
        print(f"you tie{user_action}")
#dictionary  describes the victory conditions:

def dict_winners(user_action, computer_action):
    victories={
        Action.Rock:[Action.scissors],
        Action.paper: [Action.Rock],  # Paper beats rock
        Action.scissors: [Action.paper]
    }
    defeats=victories[user_action]

    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")


def the_game():
    while True:
        try: 
            user_action = get_user_selection()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue
        computer_action = get_computer_selection()
        dict_winners = (user_action, computer_action)

        play_again = input("Play again? (y/n)")
        if play_again.lower() != "y":
            break
