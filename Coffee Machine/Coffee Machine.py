logo="""
 $$$$$$\             $$$$$$\   $$$$$$\                           $$\      $$\                     $$\       $$\                     
$$  __$$\           $$  __$$\ $$  __$$\                          $$$\    $$$ |                    $$ |      \__|                    
$$ /  \__| $$$$$$\  $$ /  \__|$$ /  \__|$$$$$$\   $$$$$$\        $$$$\  $$$$ | $$$$$$\   $$$$$$$\ $$$$$$$\  $$\ $$$$$$$\   $$$$$$\  
$$ |      $$  __$$\ $$$$\     $$$$\    $$  __$$\ $$  __$$\       $$\$$\$$ $$ | \____$$\ $$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ 
$$ |      $$ /  $$ |$$  _|    $$  _|   $$$$$$$$ |$$$$$$$$ |      $$ \$$$  $$ | $$$$$$$ |$$ /      $$ |  $$ |$$ |$$ |  $$ |$$$$$$$$ |
$$ |  $$\ $$ |  $$ |$$ |      $$ |     $$   ____|$$   ____|      $$ |\$  /$$ |$$  __$$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |$$   ____|
\$$$$$$  |\$$$$$$  |$$ |      $$ |     \$$$$$$$\ \$$$$$$$\       $$ | \_/ $$ |\$$$$$$$ |\$$$$$$$\ $$ |  $$ |$$ |$$ |  $$ |\$$$$$$$\ 
 \______/  \______/ \__|      \__|      \_______| \_______|      \__|     \__| \_______| \_______|\__|  \__|\__|\__|  \__| \_______|
                                                  
      """

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")

def resource_calc(choice):
    condition_water=MENU[choice]["ingredients"]["water"]<=resources["water"]
    if(not condition_water):
        print("Sorry there is not enough water.")
    if(choice!="espresso"):
        condition_milk=MENU[choice]["ingredients"]["milk"]<=resources["milk"]
        if(not condition_milk):
            print("Sorry there is not enough milk.")
    condition_coffee=MENU[choice]["ingredients"]["coffee"]<=resources["coffee"]
    if(not condition_coffee):
        print("Sorry there is not enough coffee.")
    if(condition_water and condition_water and condition_water):
        print("We have sufficient resources.")
        result=money_calc(choice)
        if(result=="deduct"):
            resources["water"]=resources["water"]-MENU[choice]["ingredients"]["water"]
            if(choice!= "espresso"):
                resources["milk"]=resources["milk"]-MENU[choice]["ingredients"]["milk"]
            resources["coffee"]=resources["coffee"]-MENU[choice]["ingredients"]["coffee"]
            print(f"Here is your {choice} ☕️. Enjoy!")
            
        
def money_calc(choice):
    print("\nPlease start inserting the coins: ")
    quarters=int(input("Please enter the quarters: "))
    dimes=int(input("Please enter the dimes: "))
    nickles=int(input("Please enter the nickles: "))
    pennies=int(input("Please enter the pennies: "))
    value= quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if(value>=MENU[choice]["cost"]):
        balance=value-MENU[choice]["cost"]
        money["value"]+=MENU[choice]["cost"]
        print("Transaction is successful")
        if(balance):
            print(f"Here is {round(balance,2)}$ in change.")
            return "deduct"
    else:
        print(f"Sorry that's not enough money. {value}$ refunded.")

def user_input():
    switch=True
    print("\n"*20)
    print(logo)
    while(switch):
        
        choice=input("What would you like? (espresso/latte/cappuccino): ")
        if(choice=="off"):
            print("Shutting Down. Hope you have a warm and nice day 👋")
            switch=False
        elif(choice=="report"):
            report()
        else:
            resource_calc(choice)

user_input()
        