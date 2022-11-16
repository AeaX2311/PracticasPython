#lambda
(lambda a,b : print(a+b))(1,2)

suma = lambda a,b : print(a+b)
suma(1,2)

(lambda *n : print(sum(n)))(*list(range(1,101,1)))

def multiplicador(n):
    return lambda a:print(a*n);

duplicador = multiplicador(2);
triplicador = multiplicador(3);
duplicador(11)
triplicador(10)

#input
# x = int(input("fsdfksdf"));

#trycatch
try :
    print(1/0)
except Exception as s:
    print("Error", s)
else :
    print("Sin fallas")
finally :
    print("A fuerzitas")


#assert
def suma(a,b):
    try:
        assert(type(a) == int)
        assert(type(b) == int)
    except AssertionError :
        print("Tipo de dato invalido")
    else:
        print(a+b)

suma(2,"D")
suma(2,2)