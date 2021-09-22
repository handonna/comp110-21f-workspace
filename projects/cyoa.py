"""Create Your Own Adventure"""

__author__ = "730400224"

from random import randint

points: int=0
player: str=0
emoji: str = ("\U0001f600")

def main() -> None:
    greet()
    global choice_1
    choice_1= input(f"Hello {player}, you are home alone sitting in your bedroom when you hear a weird crashing noise. Do you wish to: 1. Exit your bedroom, 2. Call someone or type 'exit' to end the game? ")
    path_1()

def greet() -> None:
    print(f"Welcome to the House Game {emoji}! In this game, you will be placed in a house where you hear an unknown sound. The objective is to make wise choices in order to figure out what is making the noise.") 
    global player
    player = input("Enter Player Name: ")

def path_1():
    if choice_1 == "1":
        print(f"Brave choice {player}! You leave your bedroom and make your way downstairs, but you hear someone moving!") 
        global points
        points = points + 1
        print(f"Point Count: {points}")
        choice_2= input(f"{player}, Do you (1) walk around and find the person or (2)stay quiet?")
        if choice_2 == "1":
            choice_3 = input(f"You decided to walk around when you hear a weird noise. Do you call out asking who it is? Yes or No")
            points = points + 1
            print(f"Point Count: {points}")
            if choice_3 == "Yes":
                print(f"Good choice, {player}, you called out and you realize it was your dog making the sounds. Mystery solved.")
                points = points + 1
                print(f"Point Count: {points}")
                print("Game Completed")
            else: 
                print("You stay quiet but soon realize the so called intruder was your dog. Mystery solved.")
                points = points + 1
                print(f"Point Count: {points}")
                print("Game Completed")
        else:
            choice_3 = (f"{player}, You stayed quiet, but hear someone coming up the stairs. Do you (1)go out and see who it is or (2)lock your door?")
            points = points + 1
            print(f"Point Count: {points}")
            if choice_3 == "1":
                print("You grab your almost dead phone and walk around the house to find that the so called intruder is your dog! Game completed.")
                points = points + 1
                print(f"Point Count: {points}")
                print("Game Completed")
            else:
                print("You lock the door and hide as you fear for your life just to find out that it was actually your dog who was running around Game completed.")
                points = points + 1
                print(f"Point Count: {points}")
                print("Game Completed")

    else:
        if choice_1 == "2":
            i = (randint(1,5))
            print(f"You pick up your phone, but quickly notice its at {i}% and is about to die.")
            points = points + 1
            print(f"Point Count: {points}")
            choice_2= input(f"Do you (1) go get the charger from the kitchen or (2) let it die?")
            if choice_2 == "1":
                choice_3 = input("Holding your pepper spray in hand, you walk out to get the charger when you hear a familiar voice say your name. Do you spray them, Yes or No?")
                points = points + 1
                print(f"Point Count: {points}")
                print("Game Completed")
                if choice_3 == "Yes":
                    print("You realize its your dog, not an intruder and you spray him with the pepper stray. Game Over.")
                    points = points + 1
                    print(f"Point Count: {points}")
                    print("Game Over")
                else:
                    print("You turn around and realize it was your dog. Good thing you refrained from spraying!")
                    points = points + 1
                    print(f"Point Count: {points}")
                    print("Game Completed")
            else:
                choice_3 = input("You let your phone die as your fear starts to grow. You realize you can't just stay in your room so you start to walk downstairs. Do you (1) take a lap around the house to see who it could be or (2) leave the house")
                if choice_3 == "Yes":
                    print("You make your way around the house to see that the noise came from your dog.")
                    points = points + 1
                    print(f"Point Count: {points}")
                    print("Game Completed")
                else:
                    print("You leave the house to see your dog through the window and realize he was the one making noise.")
                    points = points + 1
                    print(f"Point Count: {points}")
                    print("Game Completed")



       
    if choice_1 == "exit":
        print("Game over.")
        print(f"Point Count: {points}")
            

if __name__== "__main__":
    main()