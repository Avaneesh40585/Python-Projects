import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards=[11,1,2,3,4,5,6,7,8,9,10,10,10,10]
start=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if(start=='y'):
    print("\n"*100)
    print(logo)
    your_cards=random.sample(cards,2)
    bot_cards=random.sample(cards,2)
    your_score=your_cards[0]+your_cards[1]
    bot_score=bot_cards[0]+bot_cards[1]
    print(f"Your cards: [{your_cards[0]},{your_cards[1]}], current score:{your_score}")
    print(f"Computer's first card:{bot_cards[0]}")
    if(your_score==21):
        print("You have won with BlackJack")
    else:
        choice=input("Type 'y' to get another card, type 'n' to pass:")
        while(choice=='y'and your_score<21):
            your_cards.append(random.choice(cards))
            your_score=sum(your_cards)
            print(f"Your cards: {your_cards}, current score:{your_score}")
            print(f"Computer's first card:{bot_cards[0]}")
            if(your_score<21):
                choice=input("Type 'y' to get another card, type 'n' to pass:")
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        if(your_score>21):
            print(f"Computer's final hand: {bot_cards}, final score: {bot_score}")
            print("You went over. You lose")            
        else:
            while(bot_score<17):
                bot_cards.append(random.choice(cards))
                bot_score=sum(bot_cards)
            print(f"Computer's final hand: {bot_cards}, final score: {bot_score}")
            if(bot_score>21):
                print("Computer went over. You win")
            elif(your_score==21 and bot_score==21):
                print("Draw")
            elif(your_score==21):
                print("You win")
            elif(bot_score==21):
                print("You lose")
            elif(your_score==bot_score):
                print("Draw")
            elif(your_score>bot_score):
                print("You win")
            elif(your_score<bot_score):
                print("You lose")
else:
    print("Alright. Have a nice day!")