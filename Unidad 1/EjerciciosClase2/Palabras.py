"""
    Hacer un programa que lea una secuencia de palabras separadas por espacios en blanco
    que imprima las palabras en orden alfabetico, en mayusculas y sin duplicados
"""

fullCadena = input("Ingrese una cadena: ");
sett = sorted(set(fullCadena.upper().split()));
print(sett);