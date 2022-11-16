import psycopg2
from logger_base import log

class Conexion :
    _user = "postgres";
    _password = "SA";
    _host = "127.0.0.1";
    _port = "5432";
    _database = "test_db";
    _conexion = None;
    _cursor = None;

    @classmethod
    def obtenerConexion(cls) :
        if cls._conexion is None :
            try :
                cls._conexion = psycopg2.connect(
                    host = cls._host,
                    user = cls._user,
                    password = cls._password,
                    port = cls._port,
                    database = cls._database
                );

                log.info("Conexion a BD");
            except Exception as ex :
                log.error("Error al intentar conectar BD.");
                        
        return cls._conexion;
        
    @classmethod
    def obtenerCursor(cls) :
        if cls._cursor is None :
            try :
                cls._cursor = cls.obtenerConexion().cursor();                
                log.info("Cursor creado");
            except Exception as ex :
                log.error("Error al intentar conectar BD.");
        return cls._cursor;