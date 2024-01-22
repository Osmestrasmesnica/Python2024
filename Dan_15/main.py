#PYTHON DAN 15
#! IDE - PyCharm
# u sustini isto sto i VS Code ali je bas za python
#TODO proveriti sta je bolje da se korisiti

# Sajt sa style guide
# https://peps.python.org/pep-0008/

#! Coffee Machine
# Coffee Machine Program Requirements  
 


 

 
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
 
#TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino) ...***dodatne opcije(menu, report, off):​” 
# a. Check the user’s input to decide what to do next.  
# b. The prompt should show every time action has completed, e.g. once the drink is 
# dispensed. The prompt should show again to serve the next customer. 
Continue = True
money = 0
resources_water = resources['water']
resources_milk = resources['milk']
resources_coffee = resources['coffee']
    
def drink_menu():
    for coffee_type, details in MENU.items():
        print(f"{coffee_type.capitalize()} Ingredients:")
        for ingredient, quantity in details["ingredients"].items():
            print(f"- {ingredient.capitalize()}: {quantity} units")
        print(f"- Price: {details['cost']} $")
        print("\n")

#TODO 4. Check resources sufficient? 
# a. When the user chooses a drink, the program should check if there are enough 
# resources to make that drink.  
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should 
# not continue to make the drink but print: “​Sorry there is not enough water.​” 
# c. The same should happen if another resource is depleted, e.g. milk or coffee. 
def make_coffee(coffee_type, resources, money):
     # Provera da li piće postoji u resursima
    if coffee_type in ['off', "menu", "report"]:
        print("Dobrodošli u tajni MENU....")
        return False, money, resources
    elif coffee_type not in MENU:
        print("Pogrešan tip kafe. Molimo vas da izaberete espresso, latte ili cappuccino.")
        return False, money, resources
    else:
        # Dohvatanje potrebnih resursa i cene za odabrano piće
        ingredients_needed = MENU[coffee_type]["ingredients"]
        cost = MENU[coffee_type]["cost"]

        # Provera da li ima dovoljno resursa
        for ingredient, quantity in ingredients_needed.items():
            if resources[ingredient] < quantity:
                print(f"Nažalost, nemamo dovoljno {ingredient}.")
                return False, money, resources
        
        #TODO 5. Process coins. 
        # a. If there are sufficient resources to make the drink selected, then the program should 
        # prompt the user to insert coins.  
        # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 
        # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 
        # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 
        print(f"Unesite novčiće ako je cena izabranog pića: {cost}$")
        quarters = input("Koliko 0.25$ (quarters) unosite?")
        dimes = input("Koliko 0.10$ (dimes) unosite?")
        nickels = input("Koliko 0.05$ (nickels) unosite?")
        pennies = input("Koliko 0.01$ (pennies) unosite?")
        coins = int(quarters)*0.25 + int(dimes)*0.10 + int(nickels)*0.05 + int(pennies)*0.1
        #TODO 6. Check transaction successful? 
        # a. Check that the user has inserted enough money to purchase the drink they selected. 
        # E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the 
        # program should say “​Sorry that's not enough money. Money refunded.​”. 
        # b. But if the user has inserted enough money, then the cost of the drink gets added to the 
        # machine as the profit and this will be reflected the next time “report” is triggered. E.g.  
        # Water: 100ml 
        # Milk: 50ml 
        # Coffee: 76g 
        # Money: $2.5 
        # c. If the user has inserted too much money, the machine should offer change.  
        # E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal 
        # places. 
        if coins < float(cost):
            print("Izvinite, niste uneli dovoljno novca. Vraćamo Vam unet iznos...")
            return False, money, resources
        
        else:
            # Ažuriranje stanja novca
            money += cost
            #TODO 7. Make Coffee. 
            # a. If the transaction is successful and there are enough resources to make the drink the 
            # user selected, then the ingredients to make the drink should be deducted from the 
            # coffee machine resources. 

            #TODO E.g. report before purchasing latte: 
            # Water: 300ml 
            # Milk: 200ml 
            # Coffee: 100g 
            # Money: $0 
            
            #TODO Report after purchasing latte: 
            # Water: 100ml 
            # Milk: 50ml 
            # Coffee: 76g 
            # Money: $2.5 
            for ingredient, quantity in ingredients_needed.items(): #! posto se na kraju nalazi return mora da se koristi opet ovde for petlja
                resources[ingredient] -= quantity
            # b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If 
            # latte was their choice of drink. 
            print(f"Uspesno napravljen {coffee_type.capitalize()}. Cena: {cost} $.")
            print(f"Izvolite Vaš {coffee_type.capitalize()}, Uneli ste {coins}$ i Vaš kusur je {round(coins-cost, 2)}$")  
        return True, money, resources # ovaj return prekida for petlju prvu
            
while Continue:
    print("Šta želte da popijete? Upišite 'menu' da vidite izbor kafa ili unesite 'espresso', 'latte' ili 'cappuccino'..... ***(samo ta admine: 'menu', 'report', 'off' )")
    drink = input().lower()
    provera, money, resources= make_coffee(drink, resources, money)
    #print(f"{provera}, {money}, {resources}")
    if provera:
        print(f"Trenutno stanje resursa: {resources}")
        print(f"Trenutno stanje novca: {money} $")
        
    
    #TODO 2. Turn off the Coffee Machine by entering “​off​” to the prompt. 
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off 
    # the machine. Your code should end execution when this happens.
    elif drink == "off":
        print("Isključili ste aparat za kafu. Hvala Vam što brinete o potrošnji struje...")
        Continue = False

    #TODO 3. Print report. 
    # a. When the user enters “report” to the prompt, a report should be generated that shows 
    # the current resource values. e.g.  
    # Water: 100ml 
    # Milk: 50ml 
    # Coffee: 76g 
    # Money: $2.5 
    elif drink == "report":
        print(resources)
        

    elif drink == "menu":
        drink_menu()
    
    else:
        print("Nije moguće napraviti odabrano piće. Niste uneli isprvno komandu...")