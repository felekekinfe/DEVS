import random
player=input('r for rock, s for sciessor, p for paper')
computer=random.choice(['r','s','p'])

def play():
    if player==computer:
        return 'its tie'
    if is_win():
        return "you won!"
    return 'you lost'

#r>s, s>p, p>r

def is_win():
    if(player=='r' and computer=='s') or (player=='s' and computer=='p') or (player=='p' and computer=='r'):
        return True
print(play())