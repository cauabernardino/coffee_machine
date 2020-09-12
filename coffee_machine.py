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
        return False
    
    # List with coins present in Euro currency
    euro_coins = [0.01, 0.02, 0.05, 0.10, 0.20, 0.50, 1.0, 2.0]
    
    # Total change owed
    change = payment - price
    print(f"Change owed: EUR {round(change, 2)}\n")

    # Greedy algorithm initialization
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

    # Return the dict with coins as keys and amount as values
    return change_coins


def print_coins(coin_dict):
    """
    Function to print formatted final output. Prints coins with non-zero amounts.
    """
    if coin_dict:
        print(f"{'Coins':^9} {'Amount':^7}")

        for coin, amount in coin_dict.items():
            print(f"EUR {coin:.2f}: {amount:^7}")

        print(f"\nTotal coins: {sum(coin_dict.values())}")
    else:
        print("Paid! No change needed.")
    
    return 0


if __name__ == "__main__":
    
    # Initialization
    coffee_price = 0
    eur_inserted = 0

    # Loop for getting positive numbers
    try:
        while coffee_price <= 0:
            coffee_price = float(input("Insert coffee price (EUR): "))

        while eur_inserted <= 0:
            eur_inserted = float(input("Insert payment (EUR): "))
        
        while coffee_price > eur_inserted:
            print(f"EUR {round(coffee_price - eur_inserted, 2)} remaining")
            eur_inserted += float(input("Insert remaining (EUR): ")) 

        print(f"\nTotal inserted: EUR {eur_inserted}")

    except ValueError:
        print("Nice words won't pay my bills... (Actually, I just run with numbers!)")
        sys.exit(1)
    
    # Calculation of coins amount
    coins_amount = return_coins(coffee_price, eur_inserted)

    # Final printing
    print_coins(coins_amount)
    
    sys.exit(0)
