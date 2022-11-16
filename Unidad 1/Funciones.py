def funcionBasica (a : int) :
    """
        Esta es la descripcion del metodo
        a : int
            Es una variable
    """
    print("Funcion")

def funcionDiccionario(**val) :
    suma = 0
    for k,v in val.items() :
        print(k, v)
        suma+=v
    print(suma)

def funcRet() :
    a = 5
    b = 3
    return a,b

def suma1Al100() :
    suma = 0
    for i in range(1,101) :
        suma += i;
    return suma

print(suma1Al100())

# d = funcRet(); #d,f=funcRet
# print(d) 

# funcionBasica();

# d1 = { "a":1, "b":2, "c":3}
# funcionDiccionario(**d1);

# help(funcionBasica)

