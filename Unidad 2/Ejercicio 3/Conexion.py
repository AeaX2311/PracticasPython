import psycopg2 as d
import sys
from psycopg2 import pool
from logger_base import log

class Conexion :
    user = "postgres";
    password = "SA";
    host = "127.0.0.1";
    port = "5432";
    database = "test_db";
    conexion = None;
    cursor = None;
    MIN_CON = 1;
    MAX_CON = 5;
    pool = None;

    @classmethod
    def obtenerPool(cls) :
        if cls.pool is None:
            try :
                cls.pool = pool.SimpleConnectionPool(
                    cls.MIN_CON,
                    cls.MAX_CON,
                    host = cls.host,
                    user = cls.user,
                    password = cls.password,
                    port = cls.port,
                    database = cls.database                    
                );

                log.info(f"Creacion del pool {cls.pool}");
            except Exception as ex:
                log.error("Error en pool " + ex);

        return cls.pool;

    @classmethod
    def obtenerConexion(cls):
        log.info("Obtener conexion..");
        return cls.obtenerPool().getconn();

    @classmethod
    def liberarConexion(cls, conexion):
        log.info("Librar conexion..");
        cls.obtenerPool().putconn(conexion);
        
    @classmethod
    def cerrarConexiones(cls):
        log.info("Cerrar conexiones..");
        cls.obtenerPool().closeall();


if(__name__ == '__main__'):
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();
    conexion = Conexion.obtenerConexion();

           