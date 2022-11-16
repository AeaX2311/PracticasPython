"""
    Una jugueteria tiene exito en payasos y mu;ecas.
    Hace su venta por correo y logistica les cobra por peso del paquete.
    Deben calcular el peso de los payasos y mu;ecas que se dan en cada paquete de manda.
    Payaso 112g
    Mu;eca 75g

    Programa para n payasos, mu;ecas.. y calcule el peso total del paquete y precio total envio si:
    Payaso 100g $2.5
    Mu;eca 100g $2
"""

payasos = int(input("Cantidad de payasos: "));
munecas = int(input("Cantidad de muniecas: "));

pesoTotalP = 112 * payasos;
pesoTotalM = 75 * munecas;

costoTotalP = pesoTotalP * 2.5 / 100;
costoTotalM = pesoTotalM * 2 / 100;

print("+--------------------------------------+");
print("El peso total es de:", pesoTotalP + pesoTotalM);
print("El costo total sera de: ${0:,.2f}".format(costoTotalM + costoTotalP));
print("+--------------------------------------+");