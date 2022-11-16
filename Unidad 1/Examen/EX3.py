"""
    EJERCICIO 3
"""

def potencia2 (x) :
    return (x and (not (x & (x - 1))));

k = int(input("Ingresa k: "));

quebradas = 0;
segmentos = 1; # si es impar, empiezo desde 1
if k % 2 == 0 : #si es par, empiezo en 2
    segmentos = 2;

while (segmentos < k) :
    quebradas += 1;
    segmentos *= 2;

# Si es impar y es una potencia de 2, suma una quebrada y multiplicar barra
if k % 2 != 0 and potencia2(k + 1):
    segmentos *= 2;
    quebradas += 1;

print(segmentos, quebradas)
