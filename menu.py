# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            item_selection = input("Type item number: ")

            # 3. Check if the customer typed a number
            if item_selection.isdigit():
                # item_selection = int(item_selection)
                # Convert the menu selection to an integer
                item_selection = int(item_selection)

                # 4. Check if the menu selection is in the menu items
                if item_selection in menu_items.keys():
                    # Store the item name as a variable
                    selected_item = menu_items[item_selection]["Item name"]
                    # selected_item_name = selected_item["Item name"]
                    # selected_item_price = selected_item["price"]
                    # Ask the customer for the quantity of the menu item
                    quantity = input("How many would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1 

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": selected_item,
                        "Price": menu_items[item_selection]["price"],
                        "Quantity": quantity
                    })

                    # print(f"Added {quantity} x {selected_item_name} to your order.")
                    # Tell the customer that their input isn't valid

            else:
                # Tell the customer they didn't select a menu option
                print("Invalid item slection.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        if keep_ordering == 'y':
            # Keep ordering
            place_order = True
            break   # Exit the keep ordering question loop
        elif keep_ordering == 'n':
                # Complete the order
                place_order = False
                # if order_list:  # Check if there are items in the order
                    # print("Your order has been placed:")
                    # total_price = 0
                    # for item in order_list:
                        # print(f"{item['Quantity']} x {item['Item name']} at ${item['price']} each")
                        # total_price += item['price'] * item['Quantity']
                    # print(f"Total price: ${total_price:.2f}")
                # else:
                    # print("No items were ordered.")
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order")
                break # Exit the keep ordering question loop
        else:
                print("Invalid input. Please enter 'y' or 'n'.")
            
                # Tell the customer to try again
                print("Please enter 'Y' for Yes or 'N' for No.")

# Initialize total cost
total_cost = 0

# Print out the customer's order
print("\nYour order summary:")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")
print(order_list)

# 6. Loop through the items in the customer's order
for item in order_list:
    # Store dictionary values in variables
    item_name = item["Item name"]
    price = item["Price"]  # Ensure key matches how you stored the price in `order_list`
    quantity = item["Quantity"]

    # Calculate spaces for formatted printing
    spaces_for_name = 26 - len(item_name)  # Fixed width for item names
    
    # Print the item name, price, a quantity
    print(f"{item_name}{' ' * spaces_for_name}| ${price:<6.2f}| {quantity:<10}")

# Update the total cost
    total_cost += price * quantity

    # Print the item name, price, and quantity
    print(f"{item_name}{' ' * spaces_for_name}| ${price:<6.2f}| {quantity:<10}")

    # Print the total cost of the order
    print(f"\nTotal cost of the order: ${total_cost:.2f}")
    print("Thank you for your order!")

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{' ' * spaces_for_name}| ${price:<6.2f}| {quantity:<10}")
    
# Print the total cost of the order
print(f"\nTotal cost of the order: ${total_cost:.2f}")
print("Thank you for your order!")    

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
total_cost = sum(item['Price'] * item['Quantity'] for item in order_list)
print(f"\nTotal cost of the order: ${total_cost:.2f}")