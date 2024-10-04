menu = {
    1: {"name": 'expresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99},
}

def calculate_subtotal(order):
    print("calculating bill subtotal....")
    subtotal = sum(item['price'] for item in order)
    return subtotal

def calculate_tax(subtotal):
    print("calcualting tax....")
    tax = round(subtotal *0.15, 2)
    return tax

def summarize_order(order):
    print("order")
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item['name'] for item in order]
    return names, total

def print_order(order):
    print("You've ordered " + str(len(order)), ' items')
    items = [item['name'] for item in order]
    print(items)
    return order

def display_menu():
    print("----Menu----")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name']} | {menu[selection]['price']}")
    print()

def take_order():
    display_menu()
    order = []
    while True:
        try:
            item_count = int(input("How many items would you like to order? choose between 1 - 5: "))
            if 1 <= item_count <= 5:
                break
            else:
                print("Please choose a number from 1 - 5")
        except ValueError:
            print("Please enter a valid number")

    count = 1
    while count <= item_count:
        try:
            item = int(input("select menu number " + str(count) + " from 1 to 5: "))
            if item in menu:
                order.append(menu[int(item)])
                count += 1
            else:
                print("Enter a valid number")
        except Exception:
            print(" pick a number one the menu")
    return order

def main():
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("Subtotal for the order is " + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax on the order is " + str(tax))

    items, total = summarize_order(order)
    print(f"{items}")
    print(f"{total}")

if __name__ == "__main__":
    main()