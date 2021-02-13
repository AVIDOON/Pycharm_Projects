# I am going to make a rock, papers, scissors game.
# Rock beats scissor, paper beats rock and scissor beats paper.
# single player game
# continuous single input till anyone of them wins.
import random

def getRandomValue():
    listItems = ['rock','paper','scissor']
    return random.choice(listItems)

def userInputCheck(userInput,ran):
 while(userInput != ran):
    if userInput == 'paper' and ran == 'rock':
        print('You Win!')
    if userInput == 'rock' and ran == 'scissor':
        print('You Win!')
    if userInput == 'scissor' and ran == 'paper':
        print('You Win!')
    if userInput == 'rock' and ran == 'paper':
        print('You Lose!')
    if userInput == 'scissor' and ran == 'rock':
        print('You Lose!')
    if userInput == 'paper' and ran == 'scissor':
        print('You Lose!')

 elif userInput == ran:
 print('Try Again!')
 main()

def main():
   userInput = input("Say 'rock','paper' or 'scissor': ")
   ran = getRandomValue()
   print('Computer gets : '+ ran)
   userInputCheck(userInput, ran)

main()
