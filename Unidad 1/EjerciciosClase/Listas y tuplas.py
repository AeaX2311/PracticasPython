"""
    Escribir un programa que almacene las matrices, haga el producto entre ellas dos y muestre el resultado en una lista.

    Utilizar tuplas anidadas y para mostrar el resultado, listas anidadas    
"""

tuplaA = ((1, 2, 3), (4, 5, 6));
tuplaB = ((-1, 0), (0, 1), (1, 1));
lista = [[0, 0], [0, 0]];

print("--- Operaciones aplicadas: ");

contadorX = 0;
for x in tuplaA : #recorrer tuplaA
    contadorY = 0;
    
    for xx in x : #recorrer tuplaA
        contadorZ = 0;

        for y in tuplaB[contadorY] : #recorrer tuplaB
            print(" ",tuplaA[contadorX][contadorY], "X", tuplaB[contadorY][contadorZ], "=",  tuplaA[contadorX][contadorY] * tuplaB[contadorY][contadorZ]);
            lista[contadorX][contadorZ] += tuplaA[contadorX][contadorY] * tuplaB[contadorY][contadorZ];
            contadorZ += 1;
        contadorY += 1;
    contadorX += 1;

print("--- Resultado final: ");
print(" ", lista);