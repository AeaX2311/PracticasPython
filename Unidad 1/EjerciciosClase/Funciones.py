"""
    2 - Funciones
  Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada pa;abra que contiene y su frecuencia
  Escribir otra funcion que reciba el diccionario y devuelva una tupla con la palabra mas repetida y su frecuencia
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

def palabraMasRepetida(diccionario) :
    mayor = 0;
    keyMayor = "";
    for i,x in diccionario.items() :
        if(x > mayor) :
            mayor = x;
            keyMayor = i;
    
    return (keyMayor, mayor);

 

dicc = convertirADiccionario("hola jeje d d dw d d d d");
tupla2 = palabraMasRepetida(dicc);

for i,x in dicc.items() :
    print("  - Palabra: [", i, "] se repite ", x, " veces.");
print(tupla2[0], tupla2[1])
