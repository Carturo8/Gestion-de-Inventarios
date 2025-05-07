import re

inventory:dict = {}

def validate_product_name(product_name:str = ""):
    """
    Function to validate the product name.

    Parameters:
    product_name: str, name of the product.
    """
    while True:
        name = input(product_name).strip()
        if len(name) > 25:
            print("El nombre del producto no debe exceder los 25 caracteres.")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", name):
            print("Entrada inválida. Ingresa un nombre válido.")
        else:
            name = name.capitalize()
            return name

def validate_product_price(product_price:float = 0.0):
    """
    Function to validate the price of the product.

    Parameters:
    product_price: float, price of the product.
    """
    while True:
        try:
            price = round(float(input(product_price)), 2)
            if price >= 0:
                return price
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número real igual o mayor que cero.")

def validate_product_quantity(product_quantity:int = 0):
    """
    Function to validate the quantity of the product.

    Parameters:
    product_quantity: float, price of the product.
    """
    while True:
        try:
            quantity = int(input(product_quantity))
            if quantity >= 0:
                return quantity
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero igual o mayor que cero.")

def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0):
    """
    Function to add a product to the inventory.

    Parameters:
    product_name: str, name of the product.
    product_price: float, price of the product.
    product_quantity: int, quantity of the product.
    """
    condition = True
    while condition:
        name = validate_product_name("\nIngresa el nombre del producto: ")
        price = validate_product_price(f"\nIngresa el precio del producto '{name}': ")
        quantity = validate_product_quantity(f"\nIngresa la cantidad disponible del producto '{name}': ")
        inventory[name] = (price, quantity)
        print("\nDesea ingresar otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False

def search_product(product_name:str = ""):
    """
    Function to search a product in the inventory.

    Parameters:
    product_name: str, name of the product.
    """
    condition = True
    while condition:
        name = validate_product_name(f"\nIngresa el nombre del producto a buscar: ")
        name = name.capitalize()
        if name in inventory.keys():
            print(f"""
    ¡Producto encontrado!
    - Nombre del producto: '{name}'
    - Precio: ${inventory[name][0]}
    - Cantidad disponible: {inventory[name][1]}""")
            print("\nDesea buscar otro producto? (s/n): ")
            if input().lower() != "s":
                condition = False
        else:
            print("Producto no encontrado.")
            print("\nDesea agregar este producto? (s/n): ")
            if input().lower() != "s":
                print("\nDesea buscar otro producto? (s/n): ")
                if input().lower() != "s":
                    condition = False
            else:
                add_product()
    return inventory[name][0], inventory[name][1]

def update_product_price(product_name:str = "", new_product_price:float = 0.0):
    """
    Function to update the price of a product in the inventory.

    Parameters:
    product_name: str, name of the product.
    product_price: float, new price of the product.
    """
    name = validate_product_name(f"\nIngresa el nombre del producto a actualizar: ")
    if name in inventory.keys():
        new_price = validate_product_price(f"\nIngresa el nuevo precio del producto '{name}': ")
        inventory[name] = (new_price, inventory[name][1])
    else:
        print("Producto no encontrado.")

def delete_product(product_name:str = ""):
    """
    Function to delete a product from the inventory.

    Parameters:
    product_name: str, name of the product.
    """
    name = validate_product_name(f"\nIngresa el nombre del producto a eliminar: ")
    if name in inventory.keys():
        del inventory[name]
    else:
        print("Producto no encontrado.")

def calculate_total_inventory_value(inventory:dict = {}):
    """
    Function to calculate the total value of the inventory.

    Parameters:
    inventory: dict, inventory of the products.
    """
    return sum(map(lambda x: x[0], inventory.values()))

# add_product()
# search_product()
# update_product_price()
# delete_product()

print(f"\nEl inventario es: {inventory}")

#def calculate_total_inventory_value
inv = {'A': (24523.0, 2), 'C': (12345.0, 5)}
total = sum(map(lambda x: x[0], inv.values()))
print(total)