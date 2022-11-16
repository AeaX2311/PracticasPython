"""
    Implementar una funcion que reciba una palabra
    devuelva un mapa de caracteres unico en una palabra.

    El mapa es una lista numerica donde 0 corresponde con el primer caracter de la palabra,
    el 1 con el siguiente caracter y asi sucesivamente
"""

def mapaCaracteres (palabra) :
    cont = 0;
    dicc = dict();
    lista = list();

    for letra in palabra :
        if dicc.get(letra) == None :
            dicc[letra] = cont;
            cont += 1;
        
        lista.append(dicc.get(letra));
        
    return lista;

print(mapaCaracteres("aabcbda")); #[0,0,1,2,1,3,0]