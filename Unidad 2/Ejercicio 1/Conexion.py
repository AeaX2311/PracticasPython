from unittest import result
import psycopg2
from logger_base import log

conexion = psycopg2.connect(user = "postgres",  password = "SA", host = "127.0.0.1", port = "5432", database = "Python");

def selectAllPersona() :
    try:
        cursor = conexion.cursor();
        cursor.execute("SELECT id_persona, nombre, direccion FROM public.persona");
        lista = cursor.fetchall();
        return list(lista);
    except Exception as ex:
        log.error(ex);

def insertInto(values) :
    try:
        conexion.autocommit = False;
        cursor = conexion.cursor();
        query = "INSERT INTO Persona(nombre, direccion) VALUES(%s, %s)";
        valores = (values[0], values[1]);
        cursor.execute(query, valores);
        conexion.commit();

        log.info('Archivo insertado correctamente.');
    except Exception as ex:
        conexion.rollback();
        log.error(ex);
    finally:
        conexion.close();

def update(values) :
    try:
        conexion.autocommit = False;
        cursor = conexion.cursor();
        query = "UPDATE Persona SET nombre = %s, direccion = %s WHERE id_persona = %s";
        valores = (values[1], values[2], values[0]);
        cursor.execute(query, valores);
        conexion.commit();

        log.info('Archivo actualizado correctamente.');
    except Exception as ex:
        conexion.rollback();
        log.error(ex);
    finally:
        conexion.close();

# print(selectAllPersona());
# insertInto(["sadasdasd", "sdasdasd"])
update([6, "Tomas", "Direccion3"]);