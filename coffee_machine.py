#!/usr/bin/env python3

import sys

def return_coins(price, payment):
    """
    Function that checks if change is needed and, in case of need, 
    returns the lowest amount of coins as possible, considering the 8 coins
    that exists in Euro currency.
    """
    
    # Check for the need of payment
    if payment == price:
        return print("Paid! No change needed.")
    
    euro_coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0]
    
    change = payment - price
    print(f"Change owed: {round(change, 2)}\n")

    change_coins = {}
    current = max(euro_coins)
    
    # Greedy algorithm
    while change > 0:

        if change >= current:
            change -= current
            change = round(change, 2)

            if current not in change_coins.keys():
                change_coins[current] = 1
            else:
                change_coins[current] += 1
        else:
            euro_coins.remove(current)
            current = max(euro_coins)

    # Printing
    print(f"{'Coins':^8} {'Amount':^6}")

    for coin, amount in change_coins.items():
        print(f"{coin:.2f} EUR: {amount:^6}")

    return 0


if __name__ == "__main__":
    
    coffee_price = 0
    eur_inserted = 0

    try:
        while coffee_price <= 0:
            coffee_price = float(input("Insert coffee price (EUR): "))

        while eur_inserted <= 0:
            eur_inserted = float(input("Insert payment (EUR): "))
        
        while coffee_price > eur_inserted:
            print(f"{round(coffee_price - eur_inserted, 2)} EUR remaining")
            eur_inserted += float(input("Insert remaining (EUR): ")) 

        print(f"\nTotal inserted: {eur_inserted}.")

    except ValueError:
        print("Words are not currencies... yet.")
        sys.exit(1)

    return_coins(coffee_price, eur_inserted)

    sys.exit(0)