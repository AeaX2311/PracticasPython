"""
    EJERCICIO 4
"""

def convertirADiccionario(palabras) :
    list = palabras.split()
    dic = {}
    for item in list :
        if(dic.get(item) == None) : #if item in dic
            dic[item] = 1
        else :
            dic[item] = dic[item] + 1;

    return dic

def obtenerValorMayor(diccionario) :
    mayor = 0;
    for i,x in diccionario.items() :
        if x > mayor :
            mayor = x;
    return mayor;

def palabrasMasRepetidas(diccionario, mayor) :
    lista = list();
    for i, x in diccionario.items() :
        if x == mayor :
            lista.append(i);
            lista.append(x);
    
    return tuple(lista);

# Como quieres que el te quiera si el que quiero que el quiera no me quiere como quiero que el quiera
dicc = convertirADiccionario(input("Ingrese una oracion: "));
mayor = obtenerValorMayor(dicc);
print(palabrasMasRepetidas(dicc, mayor));