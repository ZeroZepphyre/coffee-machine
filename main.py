from data import MENU, resources


def check_resources(drink, res, name):
    drink_water = drink['ingredients']['water']
    drink_coffee = drink['ingredients']['coffee']
    if name != 'espresso':
        drink_milk = drink['ingredients']['milk']
        if drink_milk > res['milk']:
            print("Not enough milk.")
            return False
    if drink_water > res['water']:
        print("Not enough water.")
        return False
    if drink_coffee > res['coffee']:
        print("Not enough coffee.")
        return False
    else:
        return True


def check_money(drink, money):
    drink_price = drink['cost']
    if drink_price > money:
        return False
    else:
        return True


isRunning = True


while isRunning:
    change = 0
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffee: {resources['coffee']}\n "
              f"Money: {resources['money']}")
    elif choice == 'off':
        isRunning = False
        print("Turning off the machine.")
    else:
        isDoable = check_resources(MENU[choice], resources, choice)
        if isDoable:
            pennies = int(input("Insert pennies: "))
            nickels = int(input("Insert nickels: "))
            dimes = int(input("Insert dimes: "))
            quarters = int(input("Insert quarters: "))
            totalMoney = ((1*pennies)+(5*nickels)+(10*dimes)+(25*quarters))/100
            enoughMoney = check_money(MENU[choice], totalMoney)
            if enoughMoney:
                if totalMoney > MENU[choice]['cost']:
                    change = totalMoney - MENU[choice]['cost']
                    change = round(change, 2)
                    print(f"Here is your change: ${change}")
                resources['money'] += totalMoney - change
                if choice != 'espresso':
                    resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                print(f'Here is your {choice}. ☕')
            else:
                print("Not enough money inserted. Money refunded.")