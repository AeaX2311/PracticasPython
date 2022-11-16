"""
    Implementar una funcion llamada orden ciudades,
    recibe como parametro un diccionario con ciudades y su poblacion
    devolver lista de las ciudades de mas de 200,000 habitantes.
    Debe estar ordenada de mayor a menor
"""

def ordenaCiudades (**ciudades) :
    lista = list();

    for e in sorted(ciudades.items(), key = lambda x : x[1], reverse = True) :
        if(e[1] > 200000) :
            lista.append(e[0]);
            
    return lista;

dicc = { "NL": 32475489, "ER": 233348798253, "CT": 222, "HJ": 440000, "VT": 344};
print(ordenaCiudades(**dicc));
