import random
#user guess
def guess(x):
    count=0
    random_number=random.randint(1, x)
    guess=0
    while guess != random_number:
        guess=int(input(f'enter any number between 1 to {x}'))
        if guess > random_number:
            print(f'your guess is bigger')
            
        elif guess < random_number:
            print(f'your guess is too small')
        count+=1
    print(f'congrats, you guessed the right number within {count} try, its {random_number}' )
print(guess(x))

#computer guess
def computer(x):
    random_number=int(input('the number you want the computer to guess '))
    guess=random.randint(0, x)
    count=0
    while guess != random_number:
        guess=random.randint(0, x)
        if guess > random_number:
            print(guess)
            print('your guess is bigger')
        elif guess < random_number:
            print('your guess is too small')
            print(guess)
        count+=1
        guess=random.randint(0, x)
        
    print(f'congrats, you guessed the right number within {count} try, its {random_number}' )
print(computer(x))