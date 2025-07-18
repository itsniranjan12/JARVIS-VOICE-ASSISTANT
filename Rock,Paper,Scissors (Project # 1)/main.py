import random

''' rock = 1
    paper = -1
    scissors = 0
'''

player = int(input("Choose your option: "))
computer = random.choice([-1,0,1])
dictionary = {1:"rock",-1:"paper",0:"scissors"}
player_choice = dictionary[player]
computer_choice = dictionary[computer]




print(f"You chose {player_choice} and computer chose {computer_choice}")

if (player == computer):
    print("Draw\nTry Again")

else:
    if (player == 1) and (computer == -1):
        print("Computer wins")
    elif (player == -1) and (computer == 1):
        print("You win")
    elif (player == 1) and (computer == 0):
        print("You win")
    elif (player == 0) and (computer == 1):
        print("Computer wins")
    elif (player == -1) and (computer == 0):
        print("Computer wins")
    elif (player == 0) and (computer == -1):
        print('You win')
    else:
        print("Something went wrong")    

print('Thanks For Playing')    


