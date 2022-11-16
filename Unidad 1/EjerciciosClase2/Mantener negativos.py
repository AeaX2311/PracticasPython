"""
    Escribir una funcion ordenaPositivos que dada una lista de numeros enteros,
    devuelva una nueva lista con los numeros positivos de menor a mayor
    que mantenga los numeros negativos en la misma posicion.
"""

def ordenaPositivos (lista) :
    positivos = set(); negativosConAst = list();

    for el in lista :
        if el > 0 :
            positivos.add(el);
            negativosConAst.append("*");
        else :
            negativosConAst.append(el);
    
    positivos = list(positivos)

    x = 0; y =0;
    for el in negativosConAst :
        if el == "*" :
            negativosConAst[y] = positivos[x]
            x += 1;
        y += 1;
        
    return negativosConAst;

lista = [6, 3, -2, 0, 5, -8, 2, -2]; #[2,3,-2,5,-8,6,2]
print(ordenaPositivos(lista));