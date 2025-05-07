import re

inventory:dict = {}

def validate_product_name(product_name:str = ""):
    """
    Function to validate the product name.
    """
    condition = True
    while condition:
        product_name = input("\nIngresa el nombre del producto: ").strip()
        if len(product_name) > 25:
            print("El nombre del producto no debe exceder los 25 caracteres.")
        elif not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", product_name):
            print("El nombre del producto solo puede contener letras y espacios.")
        else:
            product_name = product_name.capitalize()
            condition = False
    return product_name

def validate_product_price(product_price:float = 0.0):
    """
    Function to validate the price of the product.
    """
    condition = True
    while condition:
        try:
            product_price = round(float(input("\nIngresa el precio del producto: ")), 2)
            if product_price >= 0:
                condition = False
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número real igual o mayor que cero.")
    return product_price

def validate_product_quantity(product_quantity:int = 0):
    """
    Function to validate the quantity of the product.
    """
    condition = True
    while condition:
        try:
            product_quantity = int(input("\nIngresa la cantidad disponible del producto: "))
            if product_quantity >= 0:
                condition = False
            else:
                print("El número debe ser positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero igual o mayor que cero.")
    return product_quantity

def request_product_data():
    """
    Function to request product data.
    """
    product_name = validate_product_name()
    product_price = validate_product_price()
    product_quantity = validate_product_quantity()
    return product_name, product_price, product_quantity

def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0):
    """
    Function to add a product to the inventory.
    """
    condition = True
    while condition:
        inventory[product_name] = (product_price, product_quantity)
        print("\nDesea ingresar otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False
        else:
            product_name, product_price, product_quantity = request_product_data()

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

def menu_1():
    """
    Function to display the first menu.
    """
    print("""\nMenú de funciones: 
    1. Añadir producto.
    2. Buscar producto.
    3. Actualizar precio.
    4. Eliminar producto.
    5. Calcular el valor total del inventario.
    6. Ver el inventario.
   --> Ingrese otro valor para salir.
    """)

def menu_2():
    """
    Function to display the second menu and return a boolean value indicating whether to continue.
    """
    print("""\nMenú de opciones:
    1. Volver al menú principal.
   --> Ingrese otro valor para salir.""")
    option = input("\nIngresa la opción deseada: ")
    condition = True
    if option == "1":
        menu_1()
    else:
        condition = False
        print("Gracias por usar el programa.")
    return condition

def main():
    """
    Function to run the program.
    """
    condition = True
    menu_1()
    while condition:
        option = input("Ingresa el número de la acción que deseas realizar: ")
        if option == "1":
            print("\n-- Añadir producto --")
            product_name, product_price, product_quantity = request_product_data()
            add_product(product_name, product_price, product_quantity)
            condition = menu_2()
        elif option == "2":
            print("\n-- Buscar producto --")
            search_product()
            condition = menu_2()
        elif option == "3":
            print("\n-- Actualizar precio --")
            update_product_price()
            condition = menu_2()
        elif option == "4":
            print("\n-- Eliminar producto --")
            delete_product()
            condition = menu_2()
        elif option == "5":
            print("\n-- Calcular el valor total del inventario --")
            print(calculate_total_inventory_value())
            condition = menu_2()
        elif option == "6":
            print("\n-- Ver el inventario --")
            print(f"\nEl inventario es: {inventory}")
            condition = menu_2()
        else:
            condition = False
            print("Gracias por usar el programa.")

if __name__ == "__main__":
    main()