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
            print("Nombre inválido. Ingrese un nombre de producto válido.")
        else:
            product_name = product_name.capitalize()
            condition = False
    return product_name.capitalize()

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
                print("Precio inválido. El precio debe ser un número igual o mayor que cero.")
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
                print("Cantidad inválida. La cantidad debe ser un número igual o mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero igual o mayor que cero.")
    return product_quantity

def add_product(product_name:str = "", product_price:float = 0.0, product_quantity:int = 0):
    """
    Function to add a product to the inventory.
    """
    condition = True
    while condition:
        inventory[product_name] = (product_price, product_quantity)
        print("\n¿Deseas añadir otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False
        else:
            product_name = validate_product_name()
            product_price = validate_product_price()
            product_quantity = validate_product_quantity()

def search_product(product_name:str = ""):
    """
    Function to search a product in the inventory.

    Parameters:
    product_name: str, name of the product.
    """
    product_price:float = 0.0
    product_quantity:int = 0
    condition = True
    while condition:
        if product_name in inventory.keys():
            print(f"""
    ¡Producto encontrado!
    - Nombre del producto: '{product_name}'
    - Precio: ${inventory[product_name][0]}
    - Cantidad disponible: {inventory[product_name][1]}""")
            product_price = inventory[product_name][0]
            product_quantity = inventory[product_name][1]
        else:
            print("El producto no se encuentra en el inventario.")
        print("\n¿Deseas buscar otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False
        else:
            product_name = validate_product_name()
    return product_price, product_quantity

def update_product_price(product_name:str = "", new_product_price:float = 0.0):
    """
    Function to update the price of a product in the inventory.

    Parameters:
    product_name: str, name of the product.
    product_price: float, new price of the product.
    """
    condition = True
    while condition:
        if product_name in inventory.keys():
            inventory[product_name] = (new_product_price, inventory[product_name][1])
            print(f"\nEl precio del producto '{product_name}' ha sido actualizado a ${new_product_price}.")
        else:
            print("\nEl producto no se encuentra en el inventario.")
        print("\n¿Deseas actualizar el precio de otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False
        else:
            product_name = validate_product_name()
            new_product_price = validate_product_price()

def delete_product(product_name:str = ""):
    """
    Function to delete a product from the inventory.

    Parameters:
    product_name: str, name of the product.
    """
    condition = True
    while condition:
        if product_name in inventory.keys():
            del inventory[product_name]
            print(f"\nEl producto '{product_name}' ha sido eliminado del inventario.")
        else:
            print("\nEl producto no se encuentra en el inventario.")
        print("\n¿Deseas eliminar otro producto? (s/n): ")
        if input().lower() != "s":
            condition = False
        else:
            product_name = validate_product_name()

def menu_1():
    """
    Function to display the first menu.
    """
    print("""\nMenú de opciones: 
    1. Añadir producto.
    2. Buscar producto.
    3. Actualizar precio.
    4. Eliminar producto.
    5. Calcular el valor total del inventario.
    6. Ver el inventario.
   --> Ingrese otro valor para salir.
    """)
    option = input("Ingresa el número de la acción que deseas realizar: ")
    return option

def menu_2():
    """
    Function to display the second menu and return a boolean value indicating whether to continue.
    """
    print("""\nMenú de opciones:
    1. Volver al menú principal.
   --> Ingrese otro valor para salir.""")
    option = input("\nIngresa la opción deseada: ")
    condition = True
    if option != "1":
        condition = False
        print("Gracias por usar el programa.")
    return condition

def main():
    """
    Function to run the program.
    """
    condition = True
    while condition:
        option = menu_1()
        if option == "1":
            print("\n-- Añadir producto --")
            product_name = validate_product_name()
            product_price = validate_product_price()
            product_quantity = validate_product_quantity()
            add_product(product_name, product_price, product_quantity)
            condition = menu_2()
        elif option == "2":
            print("\n-- Buscar producto --")
            product_name = validate_product_name()
            search_product(product_name)
            condition = menu_2()
        elif option == "3":
            print("\n-- Actualizar precio --")
            product_name = validate_product_name()
            new_product_price = validate_product_price()
            update_product_price(product_name, new_product_price)
            condition = menu_2()
        elif option == "4":
            print("\n-- Eliminar producto --")
            product_name = validate_product_name()
            delete_product(product_name)
            condition = menu_2()
        elif option == "5":
            print("\n-- Calcular el valor total del inventario --")
            total_value = sum(map(lambda x: x[0], inventory.values()))
            print(f"\nEl valor total del inventario es: ${total_value:.2f}")
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