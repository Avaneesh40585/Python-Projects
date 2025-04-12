from source import Menu, MenuItem,CoffeeMaker,MoneyMachine
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

ObjM=Menu()
ObjCM=CoffeeMaker()
ObjMM=MoneyMachine()

def Machine(choice):
    ObjMI=ObjM.find_drink(choice)
    resource_condition =ObjCM.is_resource_sufficient(ObjMI)
    if(resource_condition):
        payment_condition=ObjMM.make_payment(ObjMI.cost)
        if(payment_condition):
            print("Transaction is successful")
            ObjCM.make_coffee(ObjMI)

def Input():
    switch=True
    print("\n"*20)
    print(logo)
    while(switch):
        choice=input(f"What would you like? {ObjM.get_items()}: ")
        if(choice=="off"):
            print("Shutting Down. Hope you have a warm and nice day 👋")
            switch=False
        elif(choice=="report"):
            ObjCM.report()
            ObjMM.report()
        else:
            Machine(choice)
Input()