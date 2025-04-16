
from tkinter import *
import random
import tkinter
user = int
computer = int
win = 0
lose = 0
def rps(win, lose, user):
    computer = random.randrange(1,4)
    if user == computer:
        var.set("It's a draw. \n No Points")  
    elif user == 1 and computer == 3:
        var.set("You chose Rock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
            
    elif user == 1 and computer == 2:
        var.set("You chose Rock, I chose Paper. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 1:
        var.set("You chose Paper, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        wins.set(wins.get() - 1)    
    elif user == 2 and computer == 3:
        var.set("You chose Paper, I chose Scissors. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)   
    elif user == 3 and computer == 1:
        var.set("You chose Scissors, I chose Rock. \nYou lose")
        lose += 1
        wins.set(wins.get() - 1)    
    elif user == 3 and computer == 2:
        var.set("You chose Scissors, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 3:
        var.set("You chose Spock, I chose Scissors. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 1:
        var.set("You chose Spock, I chose Rock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 4 and computer == 5:
        var.set("You chose Spock, I chose Lizard. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 4 and computer == 2:
        var.set("You chose Spock, I chose Paper. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 1:
        var.set("You chose Lizard, I chose Rock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 2:
        var.set("You chose Lizard, I chose Paper. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 5 and computer == 3:
        var.set("You chose Lizard, I chose Scissors. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 4:
        var.set("You chose Rock, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 2 and computer == 4:
        var.set("You chose Paper, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 3 and computer == 4:
        var.set("You chose Scissors, I chose Spock. \nYou lose")
        lose +=1
        wins.set(wins.get() - 1)
    elif user == 5 and computer == 4:
        var.set("You chose Lizard, I chose Spock. \nYou win")
        wins.set(wins.get() + 1)
        
    elif user == 1 and computer == 5:
        var.set("You chose Rock, I chose Lizard. \nYou win")
        wins.set(wins.get() + 1)
        
