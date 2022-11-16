from Conexion import Conexion
from logger_base import log

class CursorPool:
    def __init__(self) -> None:
        self.conexion = None;
        self.cursor = None;

    def __enter__(self):
        log.info("metodo with");
        self.conexion = Conexion.obtenerConexion();
        self.cursor = self.conexion.cursor();
        return self.cursor;
    
    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExceptcon):
        log.info("exit")
        if valorExcepcion:
            self.conexion.rollback();
        else:
            self.conexion.commit();

        self.cursor.close();

        Conexion.liberarConexion(self.conexion);

if __name__ == '__main__':
    with CursorPool() as cursor:
        log.info("inicio metodo with");
        cursor.execute("SELECT * FROM persona");
        log.info(cursor.fetchall())