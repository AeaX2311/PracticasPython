"""
    Escribir un programa que pregunte una frase, letra.
    Imprimir cantidad de veces que se repite la letra.
"""

palabra = input("Palabra en la que se va a buscar: ");
letra = input("Letra a contar: ");
contador = 0;

for l in palabra :
    if l == letra :
        contador += 1;

print(contador);