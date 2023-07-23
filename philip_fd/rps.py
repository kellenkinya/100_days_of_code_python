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