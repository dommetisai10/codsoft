import random
ch=['rock','papper','scissor']
userinput=1
while(userinput==1):
    user=input("enter your user choice rock,papper,scissor:")
    computer=random.choice(ch)
    print("***computer choice***:",computer,"\n","***user choice***:",user)
    if user=='rock' and computer=='papper':
        print("computer is winner")
    elif computer=='rock' and user=='papper':
        print("user is winner")
    elif user=='rock' and computer=='scissor':
        print("user is winner")
    elif user=='scissor' and computer=='rock':
        print("computer is winner")
    elif user=='papper' and computer=='scissor':
        print("computer is winner")
    elif user=='scissor' and computer=='papper':
        print("user is winner")
    else:
        print("This  game is Tie")
    print("Computer if they want to play Another game\n")
    userinput1=input("enter your choice 'play or exit':")
    if userinput1=="exit":
        break
    else:
        print("************let play once again************")
