#TIPOS DE DATOS

##########Numericos
#Enteros
x=0
print(id(x),x);
#Flotantes
x=0.0
print(id(x),x)
#Complejos
x=-5j
#Conversiones a tipo de dato
print(int(3.9))
print(float(2323)+14.4)
print(complex(3))
#tuple(lista)

x = "Hola pepe"
print(x)
x='Hola pepe'
print(x+"k", f"Saludad: {x} xd", f"{x}")
print(x[::-1])

#Colecciones
tupla = (1, 2, 3)
print (tupla)
print(tupla[0])
for t in tupla : print(t)
#tupla.count(n) => cuantos elementos n hay en la tupla
#tupla.index(n) => posicion elemento n..

#Listas
lista = [1, 2.3, "ef", (2,3), [2.2,2]]
print(lista)
print(lista[3][1])
lista[0:1]=2,1
print(lista)
for index, l in enumerate(lista, 0) : print(index, l)
#zip es foreach
#range() para un for

#SETS
set = {1,2,3,4,4,4,4,3,23,234,2,5,4} #no repite y ordena
set2 = {0,678,3456,654,645,645,65,5}
# print(set.remove(2)) el elemento tiene que estar
# print(set.discard(5)) el elemento puede no estar
# otro = set.pop() #elimina el primer elemento
set3 = set2.union(set)

print("Union", set3, type(set3))
print(set)

#Tuplas 
tupla = (1,2,3)
print(tupla[1])

#Diccionarios
baseDeDatos = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 18: "dieciocho", 19: "diecinueve", 20: "veinte"};
for x,y in baseDeDatos.items() : 
    print(x,y);

print(baseDeDatos.values())
print(baseDeDatos.items())
print(baseDeDatos.keys())
print(list(baseDeDatos.keys())[0])

baseDeDatos.popitem();
baseDeDatos.pop(3)
print(baseDeDatos)