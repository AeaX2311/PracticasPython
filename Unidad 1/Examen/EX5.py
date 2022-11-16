"""
    EJERCICIO 5
"""

def generarLista(n) :
    lista = list();
    for x in range(n - 10, n) :
        lista.append(x);

    return lista;

listas = list(); mul = 11;
for x in range(0, 10) :
    aux = generarLista(mul);
    mul += 10;
    listas.append(aux);

inicio = int(input("Ingrese un numero entre 0 y 9: "));
res = 0;
for lista in listas :
    res += lista[inicio];

print(res);