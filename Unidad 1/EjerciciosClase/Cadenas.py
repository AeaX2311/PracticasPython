"""
    Escribir un programa que pregunte el nombre de un producto, precio y unidades.
    Mostrar cadena con el nombre del producto, su precio unitario con seis digitos enteros y dos decimales.
    El num de unidades con 3 digitos.
    El costo total con 8 digitos y 2 decimales.
"""

import string


nombre = input("Nombre del producto:");
precio = float(input("Precio:"));
cantidad = int(input("Cantidad:"));

print("\nResultados:");
print(" - {0} | ${1:,.2f} costo unitario | {2} unidades | ${3:,.2f} costo total.".format(nombre, precio, cantidad, precio * cantidad));