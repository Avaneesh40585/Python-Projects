from art import logo,vs
from data import data
import random
score=0
print("\n"*20)
print(logo)
current=random.sample(data,2)
person_a=current[0]
person_b=current[1]
def compare():
    global person_a,person_b,score
    print(f"Compare A:{person_a["name"]}, a {person_a["description"]}, from {person_a["country"]}")
    print(vs)
    print(f"Against B:{person_b["name"]}, a {person_b["description"]}, from {person_b["country"]}")
    choice=input("Who has more followers? Type 'A' or 'B':")
    if(choice=='A'or choice=='a'):
        if(person_a["follower_count"]>person_b["follower_count"]):
            score+=1
            print("\n"*20)
            print(logo)
            print(f"You're right! Current score: {score}.")
            person_b=random.choice(data)
            while(person_b==person_a):
                person_b=random.choice(data)
            compare()
        else:
            print(f"Sorry that's wrong. Final score: {score}")
    elif(choice=='B'or choice=='b'):
        if(person_b["follower_count"]>person_a["follower_count"]):
            score+=1
            print("\n"*20)
            print(logo)
            print(f"You're right! Current score: {score}.")
            person_a=random.choice(data)
            while(person_a==person_b):
                person_a=random.choice(data)
            compare()
        else:
            print(f"Sorry that's wrong. Final score: {score}")
    else:
        print("Invalid choice entered. Try again")
compare()