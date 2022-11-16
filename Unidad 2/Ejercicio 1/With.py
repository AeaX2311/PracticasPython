from unittest import result
import psycopg2
from logger_base import log

conexion = psycopg2.connect(user = "postgres",  password = "SA", host = "127.0.0.1", port = "5432", database = "Python");

def select() :
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "SELECT * FROM public.persona WHERE id_persona = %s";
                idPersona = input("Ingrese el ID: ");
                cursor.execute(query, idPersona);
                resultado = cursor.fetchone();
                log.info(resultado);
    except Exception as ex:
        print(ex);
    finally:
        conexion.close();

def insert():
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "INSERT INTO Persona(nombre, direccion) VALUES(%s, %s)";
                valores = (("Juan", "Dicc"), ("Fe", "Direc"), ("Antonio", "#43434"));
                cursor.executemany(query, valores);
                resultado = cursor.rowcount;
                log.info(f"Insertados: {resultado}");
    except Exception as ex:
        print(ex);
    finally:
        conexion.close();

def delete():
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "DELETE FROM Persona WHERE id_persona = %s";
                idPersona = input("Ingrese el ID: ");
                cursor.execute(query, idPersona);
                resultado = cursor.rowcount;
                log.info(f"Eliminados: {resultado}")
    except Exception as ex:
        print(ex);
    finally:
        conexion.close();

def update():
    try:
        with conexion:
            with conexion.cursor() as cursor:
                query = "UPDATE Persona SET nombre = %s, direccion = %s WHERE id_persona = %s";
                valores = (
                    ("Karla", "Jhkds #543", 7),
                    ("Lupita", "DSDFSD #2312", 8)
                );
                cursor.executemany(query, valores);
                resultado = cursor.rowcount;
                log.info(f"Actualizados: {resultado}");
    except Exception as ex:
        print(ex);
    finally:
        conexion.close();

update();