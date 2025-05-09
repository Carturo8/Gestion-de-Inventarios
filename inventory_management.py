import re

inventory:dict = {}

def validate_product_name(product_name:str = "") -> str:
    """
    Validate and format a product name according to specific rules.

    - Max 25 characters
    - Letters and spaces only (supports Spanish characters)
    - Single spaces only

    Args:
        product_name (str, optional): Initial product name to validate. Defaults to "".

    Returns:
        str: The validated and capitalized product name.
    """
    condition = True
    while condition:
        product_name = " ".join(input("\n📝 Enter the product name: ").split())
        if len(product_name) > 25:
            print("\033[91m❌ The product name must not exceed 25 characters.\033[0m")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", product_name):
            print("\033[93m⚠️ Only letters and spaces are allowed (including accents like á, é, ñ).\033[0m")
        else:
            condition = False
    print(f"\033[92m✅ Product name accepted: {product_name.capitalize()}\033[0m")
    return product_name.capitalize()

def validate_product_price(product_price:float = 0.0) -> float:
    """
    Validate and format a product price according to specific rules.

    - Must be a positive number or zero
    - Must be a valid float number
    - Rounds to 2 decimal places

    Args:
        product_price (float, optional): Initial price to validate. Defaults to 0.0.

    Returns:
        float: The validated price rounded to 2 decimal places.
    """
    condition = True
    while condition:
        try:
            product_price = round(float(input("\n💰 Enter the product price: ")), 2)
            if 0 <= product_price <= 1000000000:
                condition = False
            elif product_price > 1000000000:
                print("\033[91m❌ Price exceeds the maximum allowed ($1,000,000,000).\033[0m")
            else:
                print("\033[91m❌ Invalid price. It must be 0 or greater.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a valid number (e.g., 19.99).\033[0m")
    print(f"\033[92m✅ Price accepted: ${product_price}\033[0m")
    return product_price

def validate_product_quantity(product_quantity:int = 0) -> int:
    """
    Validate and format a product quantity according to specific rules.

    - Must be a non-negative integer
    - No decimals allowed
    - Maximum allowed quantity is 100,000,000

    Args:
        product_quantity (int, optional): Initial quantity to validate. Defaults to 0.

    Returns:
        int: The validated quantity.
    """
    condition = True
    while condition:
        try:
            product_quantity = int(input("\n📦 Enter the available product quantity: "))
            if 0 <= product_quantity <= 100000000:
                condition = False
            elif product_quantity > 100000000:
                print("\033[91m❌ Quantity exceeds the maximum allowed (100,000,000).\033[0m")
            else:
                print("\033[91m❌ Quantity must be 0 or greater.\033[0m")
        except ValueError:
            print("\033[93m⚠️ Invalid input. Please enter a whole number (e.g., 15).\033[0m")
    print(f"\033[92m✅ Quantity accepted: {product_quantity} unit(s)\033[0m")
    return product_quantity

def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0) -> None:
    """
    Add one or multiple products to the inventory.

    - Allows adding products and continuing in a loop.
    - Stores product name, price, and quantity.

    Args:
        product_name (str, optional): Name of the product. Defaults to "".
        product_price (float, optional): Price of the product. Defaults to 0.0.
        product_quantity (int, optional): Quantity of the product. Defaults to 0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition = True
    while condition:
        # Check if the product already exists
        if product_name in inventory.keys():
            print("\033[91m❌ The product is already in the inventory.\033[0m")
        else:
            inventory[product_name] = (product_price, product_quantity)
            print(f"\033[94m\n✅ Product '{product_name}':(${product_price}, {product_quantity} unit(s)) added successfully!\033[0m")
        # Ask if the user wants to add another product
        print("\n🔄 Do you want to add another product? (y/n): ", end = "")
        if input().lower() != "y":
            condition = False
        else:
            # Validate new product information
            product_name = validate_product_name()
            if product_name not in inventory.keys():
                product_price = validate_product_price()
                product_quantity = validate_product_quantity()
            else:
                print("\033[93m⚠️ The product already exists. Try a different name.\033[0m")
                continue

def search_product(product_name:str = "") -> tuple[float, int]:
    """
    Search for a product in the inventory and display its information.

    - Displays product name, price, and quantity if found.
    - Allows repeated searches.

    Args:
        product_name (str, optional): Name of the product to search. Defaults to "".

    Returns:
        tuple[float, int]: Price and quantity of the last searched product.
    """
    product_price:float = 0.0
    product_quantity:int = 0
    condition = True
    while condition:
        # Check if the product exists in the inventory
        if product_name in inventory.keys():
            product_price, product_quantity = inventory[product_name]
            print(f"""\033[94m
🔍 Product found!
🛒 Name: {product_name}
💰 Price: ${product_price}
📦 Quantity available: {product_quantity}\033[0m""")
        else:
            print(f"\033[91m❌ The product '{product_name}' is not in the inventory.\033[0m")
        # Ask if the user wants to search for another product
        print("\n🔄 Do you want to search for another product? (y/n): ", end = "")
        if input().lower() != "y":
            condition = False
        else:
            # Validate a new product name
            product_name = validate_product_name()
    return product_price, product_quantity

def update_product_price(product_name:str = "", new_product_price:float = 0.0) -> None:
    """
    Update the price of one or multiple products in the inventory.

    - Verifies if the product exists
    - Updates only the price, keeping the quantity unchanged
    - Displays confirmation and allows multiple updates

    Args:
        product_name (str, optional): Name of the product to update. Defaults to "".
        new_product_price (float, optional): New price for the product. Defaults to 0.0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition = True
    while condition:
        # Check if the product exists in the inventory
        if product_name in inventory.keys():
            old_product_price = inventory[product_name][0]
            product_quantity = inventory[product_name][1]
            inventory[product_name] = (new_product_price, product_quantity)
            print(f"""\033[94m
💱 Product price updated!
🛒 Name: {product_name}
💸 Old price: ${old_product_price}
💰 New price: ${new_product_price}
📦 Quantity available: {product_quantity}\033[0m""")
        else:
            print(f"\033[91m❌ The product '{product_name}' is not in the inventory.\033[0m")
        # Ask if the user wants to update another product's price
        print("\n🔄 Do you want to update another product's price? (y/n): ", end = "")
        if input().lower() != "y":
            condition = False
        else:
            # Validate new product information
            product_name = validate_product_name()
            new_product_price = validate_product_price()

def delete_product(product_name:str = "") -> None:
    """
    Delete one or multiple products from the inventory.

    - Verifies product existence
    - Deletes product and confirms the action
    - Allows multiple deletions in a loop

    Args:
        product_name (str, optional): Name of the product to delete. Defaults to "".

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.
    """
    condition = True
    while condition:
        # Check if the product exists in the inventory
        if product_name in inventory.keys():
            del inventory[product_name]
            print(f"\033[94m\n🗑️ The product '{product_name}' has been permanently deleted from the inventory.\033[0m")
        else:
            print(f"\033[93m⚠️ The product '{product_name}' is not in the inventory.\033[0m")
        # Ask if the user wants to delete another product
        print("\n🔄 Do you want to delete another product? (y/n): ", end = "")
        if input().lower() != "y":
            condition = False
        else:
            # Validate a new product name
            product_name = validate_product_name()

def menu() -> str:
    """
    Display the main menu of the inventory management system and get user input.

    Returns:
        str: The user's selected option as a string.
            Valid returns are "1" through "7".

    Note: This function only displays the menu and captures input.
    It does not validate the input or execute the selected operations.
    """
    print("""\nOptions Menu:
    1. Add product
    2. Search product
    3. Update price
    4. Delete product
    5. Calculate total inventory value
    6. View inventory
    7. Exit
    """)
    option = input("Enter the number of the action you want to perform: ")
    return option

def main() -> None:
    """
    Main function to run the inventory management program.

    The program continues running until the user selects the exit option (7).

    Returns:
        None: This function doesn't return any value.

    Note:
        - All user inputs are validated
        - Products are stored in the global 'inventory' dictionary
        - Monetary values are displayed with 2 decimal places
    """
    condition = True
    while condition:
        option = menu()
        if option == "1":
            print("\n-------------------- ADD PRODUCT --------------------")
            product_name = validate_product_name()
            product_price:float = 0.0
            product_quantity:int = 0
            if not product_name in inventory.keys():
                product_price = validate_product_price()
                product_quantity = validate_product_quantity()
            add_product(product_name, product_price, product_quantity)
        elif option == "2":
            print("\n-------------------- SEARCH PRODUCT --------------------")
            product_name = validate_product_name()
            search_product(product_name)
        elif option == "3":
            print("\n-------------------- UPDATE PRICE --------------------")
            product_name = validate_product_name()
            new_product_price = validate_product_price()
            update_product_price(product_name, new_product_price)
        elif option == "4":
            print("\n-------------------- DELETE PRODUCT --------------------")
            product_name = validate_product_name()
            delete_product(product_name)
        elif option == "5":
            print("\n-------------------- CALCULATE TOTAL INVENTORY VALUE --------------------")
            total_value = sum(map(lambda x: x[0] * x[1], inventory.values()))
            print(f"\nThe total inventory value is: $ {total_value:.2f}")
        elif option == "6":
            print("\n-------------------- VIEW INVENTORY --------------------\n")
            if inventory:
                print(f"{'Product Name':<25}  {'Price':<17}  {'Available Quantity':<15}")
                print("-" * 65)
                for product, details in inventory.items():
                    price, quantity = details
                    print(f"{product:<25}  $ {price:<15.2f}  {quantity:<15}")
            else:
                print("The inventory is empty.")
        elif option == "7":
            condition = False
            print("\nThank you for using the inventory management program. Goodbye!")
        else:
            print("\nIncorrect option. Please enter a valid option.")

if __name__ == "__main__":
    main()