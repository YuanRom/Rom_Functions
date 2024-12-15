print("Kamusta, Welcome sa KAINAN ni NAUY\nHere is our menu")
print("========= MENU =========")
menu = ["Sisig", "Hotdog", "Chicken", "Lumpia"]
price = [82.00, 60.00, 85.00, 60.00]

for i in range(len(menu)):
    print(f"{menu[i]}: ₱{price[i]}")

total = 0 
listahan = []

while True:
    order = input("(Enter 'done' if finished)\nWhat would you like to order?: ")

    if order.lower() == 'done':
        break
    elif order in menu:
        item_index = menu.index(order)
        total += price[item_index]
        listahan.append(order) 
        print(f"You added: {order}. Total so far: ₱{total:.2f}")
    else:
        print("Invalid item. Please order again.")

    order2 = input("Would you like to add anything else? yes/no: ")
    if order2.lower() == "no":
        if len(listahan) == 0:
            print("You did not order anything. Let us know when you're ready")
            exit ()
    if order2.lower() == "no":
        print(f"Alright, here's your order {listahan}, your total is ₱{total:.2f} Thank you for your order!")
        break
    elif order2.lower() != "yes":
        print("Invalid response. Please answer with 'yes' or 'no'.")

while True:
    payment = float(input("Please enter the amount of payment: ₱ "))
    if payment < total:
        print("Insufficient amount, Please enter the right amount.")
    elif payment > total:
        forchange = payment - total
        print(f"I received ₱{payment:.2f}. Your change is ₱{forchange:.2f}.")
        print("Thank you so much for your purchase! Have a great day.")
        break
    elif payment == total:
        print("I received the exact amount. Thank you so much for your purchase! Have a great day.")
        break
    else:
        print("Invalid! Please input the correct amount.")