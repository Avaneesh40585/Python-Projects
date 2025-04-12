import random
logo="""
   ______                        __  ___         _   __                __             
  / ______  _____  __________   /  |/  __  __   / | / __  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/  / /|_/ / / / /  /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  (__  )  / /  / / /_/ /  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/  /_/  /_/\__, /  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                    /____/                                            
    """
print("\n"*20)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
my_number=random.randint(1,100)
Difficulty_level=input("Choose a difficulty. Type 'easy' or 'hard':")
if(Difficulty_level=="easy"):
    attempts=10
elif(Difficulty_level=="hard"):
    attempts=5
else:
    print("Invalid input given")
for i in range(attempts,0,-1):
    print(f"You have {i} attempts remaining to guess the number.")
    your_number=int(input("Make a guess:"))
    if(my_number==your_number):
        print(f"You got it. The answer was:{my_number}\n")
        break
    elif(my_number>your_number):
        print("It's higher than you think it is.\n")
    elif(my_number<your_number):
        print("It's lower than you think it is.\n")
if(my_number==your_number):
    print("Congratulations, You won")
else:
    print(f"Game Over, You lost the answer was {my_number}")
    
