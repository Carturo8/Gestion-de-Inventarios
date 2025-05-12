# Programa de Gestión de Inventarios

### English version
[Click here to see the README in English](https://github.com/Carturo8/Inventory-Management/blob/main/README.md)

----

Este programa en Python ayuda a gestionar eficientemente el inventario de una tienda. Proporciona funcionalidades para añadir, buscar, actualizar, eliminar productos y calcular el valor total del inventario.

## Características
- **Añadir productos**: Permite añadir productos nuevos con su nombre, precio y cantidad.
- **Buscar productos**: Buscar un producto por su nombre y ver sus detalles (precio y cantidad).
- **Actualizar precios de productos**: Cambiar el precio de un producto existente.
- **Eliminar productos**: Eliminar productos del inventario.
- **Calcular valor del inventario**: Calcular el valor total de todos los productos en stock.

## Cómo Funciona
- El programa utiliza **funciones** para manejar cada operación (añadir, buscar, actualizar y eliminar productos).
- Los productos se almacenan en un **diccionario**, donde el nombre del producto es la clave y el precio y la cantidad se almacenan como una tupla.
- El **valor total del inventario** se calcula utilizando una función lambda.

## Funciones
1. **`validate_product_name`**: Valida y formatea los nombres de los productos (máximo 25 caracteres, solo letras y espacios).
2. **`validate_product_price`**: Valida el precio del producto (número flotante positivo, máximo 1,000,000,000).
3. **`validate_product_quantity`**: Valida la cantidad del producto (entero positivo, máximo 100,000,000).
4. **`add_product`**: Añade un producto al inventario si no existe ya.
5. **`search_product`**: Busca un producto por nombre y muestra sus detalles.
6. **`update_product_price`**: Actualiza el precio de un producto existente.
7. **`delete_product`**: Elimina un producto del inventario.
8. **`menu`**: Muestra las opciones del menú para que el usuario elija.
9. **`main`**: La función principal que controla el flujo del programa.

## Cómo Usar
- El programa pedirá al usuario que seleccione una operación hasta que decida salir.
- Para cada operación, se pedirá al usuario que ingrese los detalles necesarios.
- Si cualquier entrada es inválida, el programa pedirá al usuario que ingrese la información correcta.
- El programa calcula y muestra el valor total del inventario cuando se solicita.

## Requisitos
- Python 3.x o superior.

## Ejemplo
Se te pedirá que elijas una de las siguientes opciones:
1. Añadir producto
2. Buscar producto
3. Actualizar precio
4. Eliminar producto
5. Ver valor total del inventario
6. Salir

## Instalación
Para usar el programa, simplemente clona este repositorio y ejecuta el script `inventory_management.py`.

```bash
git clone https://github.com/yourusername/inventory-management.git
cd inventory-management
python inventory_management.py
```

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](https://github.com/Carturo8/Inventory-Management/blob/main/LICENSE) para más detalles.
