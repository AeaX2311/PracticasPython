from Persona import persona
from Conexion import conexion

class PersonaDao:
    _SELECT = "SELECT * FROM persona ORBER BY nombre";
    _INSERT = "INSERT INTO persona (nombre, apellido, correo_electronico, edad) VALUES (%s,%s,%s,%s)";
    _UPDATE = "UPDATE persona SET nombre = %s, apellido = %s, correo_electronico = %s, edad = %s WHERE id_persona = %s";
    _DELETE = "DELETE FROM persona WHERE id_persona = %s";

    # @classmethod
    # def selectAllPersona(cls) :
    #     try:
    #         cursor = conexion.obtenerCursor();
    #         cursor.execute(cls._SELECT)
    #         registros = cursor.fetchall();
    #         personas = [];
    #         for r in registros:
    #             p = persona(r[0], r[1], r[2], r[3], r[4])
    #             personas.append(r);

    #         return list(personas);
    #     except Exception as ex:
    #         conexion.log.error(ex);

    # @classmethod
    # def insertInto(values) :
    #     try:
    #         conexion = conexion.obtenerConexion();
    #         cursor = conexion.obtenerCursor();
    #         query = "INSERT INTO Persona(nombre, direccion) VALUES(%s, %s)";
    #         valores = (values[0], values[1]);
    #         cursor.execute(query, valores);
    #         conexion.commit();

    #         conexion.log.info('Archivo insertado correctamente.');
    #     except Exception as ex:
    #         conexion.rollback();
    #         conexion.log.error(ex);
    #     finally:
    #         conexion.close();

    # @classmethod
    # def update(values) :
    #     try:
    #         conexion = conexion.obtenerConexion();
    #         conexion.autocommit = False;
    #         cursor = conexion.obtenerCursor();
    #         query = "UPDATE Persona SET nombre = %s, direccion = %s WHERE id_persona = %s";
    #         valores = (values[1], values[2], values[0]);
    #         cursor.execute(query, valores);
    #         conexion.commit();

    #         conexion.log.info('Archivo actualizado correctamente.');
    #     except Exception as ex:
    #         conexion.rollback();
    #         conexion.log.error(ex);
    #     finally:
    #         conexion.close();