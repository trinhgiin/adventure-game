import time
import random
items = []
def printp(message):
    print(message)
    time.sleep(1)

def intro():
    printp("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    printp("Rumor has it that a dragon is somewhere around here, and has been terrifying the nearby village.") 
    printp("In front of you is a house.") 
    printp("To your right is a dark cave.") 
    printp("In your hand you hold your trusty (but not very effective) dagger.") 

def again_or_quit():
    response = input("Would you want to play again? (y/n) ").lower()   
    if response == "n":
        printp("Thanks for playing! See you next time.")
    elif response == "y":
        printp("Excellent! Restarting the game...")  
        play_game()
    else:
        again_or_quit()    
    

def cave():
    printp("You peer cautiously into the cave.")
    if "sword" in items:
        printp("You've been here before, and gotten all the good stuff. It's just an empty cave now.")
    else:
        printp("It turns out to be only a very small cave.")
        printp("Your eye catches a glint of metal behind a rock.")
        printp("You have found the magical Sword of Ogoroth!")
        printp("You discard your silly old dagger and take the sword with you.")
        items.append("sword")
    printp("You walk back out to the field.")
    field()
    

def house():
    monster = random.choice(["wicked fairie","gorgon","troll","witch"])
    printp("You approach the door of the house.")
    printp(f"You are about to knock when the door opens and out steps a {monster}.")
    printp(f"Eep! This is the {monster}'s house!")
    printp(f"The {monster} attacks you!")
    response = input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        if "sword" in items:
            printp(f"As the {monster} moves to attack, you unsheath your new sword.")
            printp("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
            printp(f"But the {monster} takes one look at your shiny new toy and runs away!")
            printp(f"You have rid the town of the {monster}. You are victorious!")
            again_or_quit()
        else:
            printp("You do your best...")   
            printp(f"but your dagger is no match for the {monster}.")
            printp("You have been defeated!")
            again_or_quit()
    elif response == "2":
        printp("You run back into the field. Luckily, you don't seem to have been followed.")
        field()
    else:
        again_or_quit()      

def field():
    printp("\nEnter 1 to knock on the door of the house.")
    printp("Enter 2 to peer into the cave.")
    printp("What would you like to do?")
    response = input("(Please enter 1 or 2)\n")
    if response == "1":
        house()
    elif response == "2":
        cave()    
    else:
        field()

def play_game():
    intro()
    field()

play_game()    