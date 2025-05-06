"""Añadir productos:

    Cada producto debe estar definido por su nombre, precio y cantidad disponible
    Esta información será almacenada de modo que el inventario pueda crecer dinámicamente
"""


condition = True
inventory = {}
while condition:
    name = input("Ingrese el nombre del producto: ")
    price = float(input(f"Ingrese el precio del producto '{name}': "))
    quantity = int(input(f"Ingrese la cantidad disponible del producto '{name}':"))
    inventory[name] = {"Precio": price, "Cantidad": quantity}
print(inventory)