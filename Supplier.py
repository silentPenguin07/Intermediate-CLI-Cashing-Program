price_items = {
    'apple': 45,
    'onion': 56,
    'celery': 89,
    'crab': 27,
    'mango': 67,
    'chicken': 540,
    'beef': 700,
    'fish': 563,
    'souvenir': 2400,
    'cherry': 40
}

inventory_items = {
    'apple': 5023,
    'onion': 7800,
    'celery': 450,
    'crab': 880,
    'mango': 22102,
    'chicken': 560,
    'beef': 968,
    'fish': 7289,
    'souvenir': 23
}

basket = {}

# total_before_tax = 0
# tax = 0.15
# total_after_tax = 0

def view():
    print(inventory_items)

def view_basket():
    print(basket)

def add_to_basket(addItem, quantity):
    basket[addItem] = quantity
    print(basket)

def rem_from_basket(rem_item):
    del basket[rem_item]

def check_basket(check_item):
    if check_item in basket: 
        print("This item is in your basket.")
    else: 
        print("This item is not in your basket.")

def count_basket():
    print(len(basket.keys()))

def clear_basket():
    confirm = input("Are you sure you want to clear your basket? >").lower()
    if confirm == "yes":
        basket.clear()
    else:
        print("Your basket was not cleared because you did not enter 'yes'.")
    input("Press enter to continue")

def calc_subtotal(shopping_cart):
    e = sum(shopping_cart[k] * price_items[k] for k in shopping_cart)
    return e

def save_to_file(username, email, order, total_charge):
    with open("Supplier Test Program.txt", "a") as data:
        data.write(f"Name: {username}\n")
        data.write(f"Email: {email}\n")
        data.write(f"Order: {order}\n")
        data.write(f"Total Charge: {total_charge}\n\n")

while True:

    print("""
    Select:
    [1] view inventory items
    [2] view basket
    [3] add to basket
    [4] remove from basket
    [5] check if item is in basket
    [6] how many items in basket   
    [7] clear basket
    [8] exit 
    """)

    selection = input(">")

    if selection == "1":
        view()
        input("Press enter to continue.")

    elif selection == "2":
        view_basket()

    elif selection == "3":
        try:
            to_add = input("Enter item >")
            to_quan = int(input("Quantity: >"))
            if to_add in inventory_items and to_quan <= inventory_items[to_add] :
                add_to_basket(to_add, to_quan)
            else:
                error = input("This item either does not exist or is too large in quantity. Press enter to try again. ")
            input("Press enter to continue.")
        except ValueError:
            print("You entered an incorrect variable.")
            input("Press enter to continue.")
    
    elif selection == "4":
        to_rem = input("Enter an item to remove.")
        rem_from_basket(to_rem)
    
    elif selection == "5":
        user_check = input(">")
        check_basket(user_check)
        input("Press enter to continue")
    
    elif selection == "6":
        count_basket()
        input("Press enter to continue")

    elif selection == "7":
        clear_basket()
        input("Press enter to continue")
    
    elif selection == "8":
        print(basket)
        break
    
    else:
        print("Invalid")
        input("Press enter to continue")

subtotal = calc_subtotal(basket)
print("Below is your subtotal.")
print(float(subtotal))
input("Press enter to continue.")

tax = 0.15
tax_amount = subtotal * tax
print("Below is your tax amount.")
print(tax_amount)
input("Press enter to continue.")

total_after_tax = subtotal + tax_amount
print("Below is your total charge.")
print(total_after_tax)

name = input("Username: ")
email_address = input("Email: ")
save_to_file(name, email_address, basket, total_after_tax)