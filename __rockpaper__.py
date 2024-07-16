import random
def rock_paper():
    choices=['rock','paper','scissors']
    comp_choice=random.choice(choices)
    user_choice=input("Your choice(rock, scissors, paper): ").lower()
    print(f'The computer has chosen:{comp_choice}')
    if user_choice==comp_choice:
        print("Draw")
    elif (user_choice=='rock'and comp_choice=='scissors') or (user_choice=='scissors' and comp_choice=='paper') or (user_choice =='paper' and comp_choice=='rock') :
        print("You have won")
    else :
        print("You've lost")
rock_paper()