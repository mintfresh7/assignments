# Author : Abigail Leppo
# Class : ITN160
# Class Section : 201
# Date : 11/1/23
# Assignment : Project 2 Sales System
menu = {
    1: ("soda", 1.99),
    2: ("burger", 4.99),
    3: ("hot dog", 3.99),
    4: ("fries", 2.99),
    5: ("pizza", 6.99),
    6: ("soup", 3.99)
}

def display_menu():
    print("Welcome to Beachside Restaurant! Please order from 1-6:")
    for item_num, (item, price) in menu.items():
        print(f"{item_num}: {item} (${price})")

def place_order():
    total_amount = 0
    order = []
    while True:
        display_menu()
        choice = input("Enter the number of the item you'd like to order (0 to finish): ")
        if choice == "0":
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(menu):
            item, price = menu[int(choice)]
            order.append(item)
            total_amount += price
            print(f"You ordered: {item}")
        else:
            print("Invalid choice. Please try again.")
    print(f"Your total amount is: ${total_amount:.2f}")
    print("You ordered:", ", ".join(order))

place_order()