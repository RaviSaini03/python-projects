import random
print("Welcome, to Rock, Paper, Scissor Game.\n")
repeat = 'yes'

while repeat == 'yes':

    #computer Choice
    elements = ['rock', 'paper', 'scissor']
    choiceOfComputer = random.choice(elements)

    #Manual Choice
    manualChoice = input("Enter your Choice (rock/paper/scissor): ").strip().lower()

    if(choiceOfComputer == manualChoice):
        print("Draw")
        print("Choice of Computer was: ", choiceOfComputer)
    elif(choiceOfComputer == 'rock' and manualChoice == 'paper') or  (choiceOfComputer == 'paper' and manualChoice == 'scissor') or (choiceOfComputer == 'scissor' and manualChoice == 'rock'):
        print("You Won!")
        print("Choice of Computer was: ", choiceOfComputer)
    elif(choiceOfComputer == 'paper' and manualChoice == 'rock') or (choiceOfComputer == 'scissor' and manualChoice == 'paper') or (choiceOfComputer == 'rock' and manualChoice == 'scissor'):
        print("You Lost!")
        print("Choice of Computer was: ", choiceOfComputer)
    else:
        print("Invalid Choice!\n!")
    repeat = input('Do you want to play again (yes/no): ').strip().lower()

print("\nThanks For Playing!!")
