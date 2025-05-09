import re

inventory:dict = {}

def validate_product_name(product_name:str = "") -> str:
    """
    Validate and format a product name according to specific rules.

    This function ensures that the product name meets the following criteria:
    - Maximum length of 25 characters
    - Contains only letters and spaces
    - Supports Spanish characters (á, é, í, ó, ú, ñ)

    Args:
        product_name (str, optional): Initial product name to validate. Defaults to "".

    Returns:
        str: The validated and capitalized product name.
    """
    condition = True
    while condition:
        product_name = input("\nEnter the product name: ").strip()
        if len(product_name) > 25:
            print("The product name must not exceed 25 characters.")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", product_name):
            print("Invalid name. Please enter a valid product name.")
        else:
            product_name = product_name.capitalize()
            condition = False
    return product_name.capitalize()

def validate_product_price(product_price:float = 0.0) -> float:
    """
    Validate and format a product price according to specific rules.

    This function ensures that the product price meets the following criteria:
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
            product_price = round(float(input("\nEnter the product price: ")), 2)
            if product_price >= 0:
                condition = False
            else:
                print("Invalid price. Price must be a number equal to or greater than zero.")
        except ValueError:
            print("Invalid input. Enter a real number equal to or greater than zero.")
    return product_price

def validate_product_quantity(product_quantity:int = 0) -> int:
    """
    Validate and format a product quantity according to specific rules.

    This function ensures that the product quantity meets the following criteria:
    - Must be a positive integer or zero
    - Cannot be a decimal number

    Args:
        product_quantity (int, optional): Initial quantity to validate. Defaults to 0.

    Returns:
        int: The validated quantity as an integer.
    """
    condition = True
    while condition:
        try:
            product_quantity = int(input("\nEnter the available product quantity: "))
            if product_quantity >= 0:
                condition = False
            else:
                print("Invalid quantity. Quantity must be a number equal to or greater than zero.")
        except ValueError:
            print("Invalid input. Enter an integer equal to or greater than zero.")
    return product_quantity

def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0) -> None:
    """
    Add one or multiple products to the inventory.

    This function allows adding products to the inventory and provides the option
    to continue adding more products in a loop. For each product, it stores:
    - Product name
    - Product price
    - Product quantity

    Args:
        product_name (str, optional): Name of the product. Defaults to "".
        product_price (float, optional): Price of the product. Defaults to 0.0.
        product_quantity (int, optional): Quantity of the product. Defaults to 0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.

    Note: The inventory is modified using a global dictionary where products are stored
    as tuples containing (price, quantity).
    """
    condition = True
    while condition:
        if product_name in inventory.keys():
            print("\nThe product is already in the inventory.")
        else:
            inventory[product_name] = (product_price, product_quantity)
        print("\nDo you want to add another product? (y/n): ")
        if input().lower() != "y":
            condition = False
        else:
            product_name = validate_product_name()
            if not product_name in inventory.keys():
                product_price = validate_product_price()
                product_quantity = validate_product_quantity()
            else:
                continue

def search_product(product_name:str = "") -> tuple[float, int]:
    """
    Search for a product in the inventory and display its information.

    This function allows searching for products in the inventory and provides the option
    to continue searching for more products in a loop. For each found product, it displays:
    - Product name
    - Product price
    - Product quantity

    Args:
        product_name (str, optional): Name of the product to search. Defaults to "".

    Returns:
        tuple[float, int]: A tuple containing:
            - float: Price of the last searched product (0.0 if not found)
            - int: Quantity of the last searched product (0 if not found)

    Note: The function returns the information of the last product searched,
    even if multiple searches were performed during execution.
    """
    product_price:float = 0.0
    product_quantity:int = 0
    condition = True
    while condition:
        if product_name in inventory.keys():
            print(f"""
        Product found!
        - Product name: '{product_name}'
        - Price: ${inventory[product_name][0]}
        - Available quantity: {inventory[product_name][1]}""")
            product_price = inventory[product_name][0]
            product_quantity = inventory[product_name][1]
        else:
            print("The product is not in the inventory.")
        print("\nDo you want to search for another product? (y/n): ")
        if input().lower() != "y":
            condition = False
        else:
            product_name = validate_product_name()
    return product_price, product_quantity

def update_product_price(product_name:str = "", new_product_price:float = 0.0) -> None:
    """
    Update the price of one or multiple products in the inventory.

    This function allows updating the price of products in the inventory and provides
    the option to continue updating more product prices in a loop. For each update:
    - Verifies the product exists in inventory
    - Updates the price while maintaining the original quantity
    - Confirms the update to the user

    Args:
        product_name (str, optional): Name of the product to update. Defaults to "".
        new_product_price (float, optional): New price for the product. Defaults to 0.0.

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.

    Note: The inventory is modified using a global dictionary where products are stored
    as tuples containing (price, quantity). Only the price is updated, keeping the
    original quantity intact.
    """
    condition = True
    while condition:
        if product_name in inventory.keys():
            inventory[product_name] = (new_product_price, inventory[product_name][1])
            print(f"\nThe price of product '{product_name}' has been updated to ${new_product_price}.")
        else:
            print("\nThe product is not in the inventory.")
        print("\nDo you want to update another product's price? (y/n): ")
        if input().lower() != "y":
            condition = False
        else:
            product_name = validate_product_name()
            new_product_price = validate_product_price()

def delete_product(product_name:str = "") -> None:
    """
    Delete one or multiple products from the inventory.

    This function allows removing products from the inventory and provides the option
    to continue deleting more products in a loop. For each deletion:
    - Verifies the product exists in inventory
    - Removes the product completely from the inventory
    - Confirms the deletion to the user

    Args:
        product_name (str, optional): Name of the product to delete. Defaults to "".

    Returns:
        None: This function modifies the inventory directly and doesn't return a value.

    Note: The deletion is permanent and removes all associated information (price and quantity)
    for the specified product from the inventory.
    """
    condition = True
    while condition:
        if product_name in inventory.keys():
            del inventory[product_name]
            print(f"\nThe product '{product_name}' has been deleted from the inventory.")
        else:
            print("\nThe product is not in the inventory.")
        print("\nDo you want to delete another product? (y/n): ")
        if input().lower() != "y":
            condition = False
        else:
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
            print(f"\nThe total inventory value is: ${total_value:.2f}")
        elif option == "6":
            print("\n-------------------- VIEW INVENTORY --------------------")
            print(f"\nThe inventory is: {inventory}")
        elif option == "7":
            condition = False
            print("\nThank you for using the inventory management program. Goodbye!")
        else:
            print("\nIncorrect option. Please enter a valid option.")

if __name__ == "__main__":
    main()