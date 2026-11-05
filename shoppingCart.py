# Import datetime
import datetime

# Function for determining discount
def find_discount(subtotal):
    if subtotal >= 40:
        return .15
    elif subtotal >= 20:
        return .1
    elif subtotal >= 10:
        return .05
    else:
        return 0

# Function for calculating amount saved
def find_amount_saved(subtotal, discount):
    return subtotal * discount

# Function for calculating final total
def find_final_total(subtotal, amount_saved):
    return subtotal - amount_saved

# Function for printing main menu
def main_menu():
    print("========== SMART SHOPPING CART ==========")
    print()
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")

# Function for printing an empty line.... (hi)
def what():
    print()

# Creating the products and prices
products = {
    "Ice Cream": 6.99,
    "Cheese": 3.49,
    "Milk": 7.00,
    "Yogurt": 3.29,
    "Pizza": 10.99
}

# Making shopping cart
shopping_cart = {}

# Creating Main Menu
while True:
    main_menu()

    # Getting the choice
    choice = int(input("Enter your choice: "))

    # Option 1
    if choice == 1:
        i = 1
        for product, price in products.items():
            print(str(i) + ".", format(product, "10s"), "$" + format(price, ".2f"))
            i += 1
        print()

    # Option 2
    elif choice == 2:
        i = 1
        for product, price in products.items():
            print(str(i) + ".", format(product, "10s"), "$" + format(price, ".2f"))
            i += 1
        while True:
            user_input = int(input("Enter product number: "))
            if user_input < 1 or user_input > 5:
                print("Invalid product number")
                continue
            else:
                if user_input == 1: item = "Ice Cream"
                elif user_input == 2: item = "Cheese"
                elif user_input == 3: item = "Milk"
                elif user_input == 4: item = "Yogurt"
                else: item = "Pizza"
            # Determining quantity
            while True:
                quantity = int(input(f"How many {item}s would you like to add? "))
                if quantity <= 0:
                    print("Not valid quantity")
                else: break
            # Adding to cart
            print(f"Added {quantity} {item}(s) to your cart!")
            if item not in shopping_cart:
                shopping_cart[item] = quantity
            else:
                shopping_cart[item] += quantity
            print(f"{item} quantity is now {shopping_cart[item]}")
            print()
            break

    # Option 3
    elif choice == 3:
        if len(shopping_cart) == 0:
            print("Cart is empty")
        else:
            i = 1
            temp_list = []
            for product, quantity in shopping_cart.items():
                print(str(i) + ".", format(product, "10s"), "Quantity:", quantity)
                i += 1
                temp_list.append(product)
            removed_item = int(input("Enter item number to remove: "))
            removed_item = temp_list[removed_item-1]
            print(f"Removed 1 {removed_item} from your cart!")
            shopping_cart[removed_item] -= 1
            print(f"{removed_item} quantity is now {shopping_cart[removed_item]}")
            if shopping_cart[removed_item] == 0:
                shopping_cart.pop(removed_item)
        print()

    # Option 4
    elif choice == 4:
        if len(shopping_cart) == 0:
            print("Cart is empty.")
        else:
            print("   Product    Unit Price    Quantity    Line Total")
            i = 1
            total_items = 0
            subtotal = 0
            for product, quantity in shopping_cart.items():
                line_total = quantity * products[product]
                print(str(i) + ".", format(product, "10s"), "$" + format(products[product], ".2f"), format(quantity,">9d"), format("$" + format(line_total,".2f"), ">20s"))
                i += 1
                total_items += quantity
                subtotal += line_total
            print()
            print("Total Items:", total_items)
            print("Subtotal: " + "$" + format(subtotal, ".2f"))
        print()

    # Option 5
    elif choice == 5:
        subtotal = 0
        for product, quantity in shopping_cart.items():
            line_total = quantity * products[product]
            subtotal += line_total
        print("Subtotal: $" + format(subtotal,".2f"))
        print()

    # Option 6
    elif choice == 6:
        subtotal = 0
        for product, quantity in shopping_cart.items():
            line_total = quantity * products[product]
            subtotal += line_total
        discount = find_discount(subtotal)
        amount_saved = find_amount_saved(subtotal,discount)
        final_total = find_final_total(subtotal,amount_saved)
        # Check if cart is empty
        if subtotal == 0:
            print("Cannot checkout.")
        # Print receipt
        else:
            print("========== RECEIPT ==========")
            print("Date:",datetime.datetime.today().date())
            what()
            print("   Product    Unit Price    Quantity    Line Total")
            i = 1
            total_items = 0
            for product, quantity in shopping_cart.items():
                line_total = quantity * products[product]
                print(str(i) + ".", format(product, "10s"), "$" + format(products[product], ".2f"), format(quantity,">9d"), format("$" + format(line_total,".2f"), ">20s"))
                i += 1
                total_items += quantity
            print()
            print("Total Items:", total_items)
            print("Subtotal: " + "$" + format(subtotal, ".2f"))
            print("Discount: " + str(int(discount * 100)) + "%")
            print("Amount Saved: $" + format(amount_saved,".2f"))
            print("Final Total: $" + format(final_total,".2f"))
            what()
            print("Thank you for shopping!")
            break
    