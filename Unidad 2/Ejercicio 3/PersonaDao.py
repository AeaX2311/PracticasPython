from Persona import Persona
from Conexion import Conexion
from CursorPool import CursorPool
from logger_base import log

class PersonaDao:
    _SELECT = "SELECT * FROM persona ORBER BY nombre";
    _INSERT = "INSERT INTO persona (nombre, apellido, correo_electronico, edad) VALUES (%s,%s,%s,%s)";
    _UPDATE = "UPDATE persona SET nombre = %s, apellido = %s, correo_electronico = %s, edad = %s WHERE id_persona = %s";
    _DELETE = "DELETE FROM persona WHERE id_persona = %s";

    @classmethod
    def selectAllPersona(cls) :
        try:
            with CursorPool() as cursor:                    
                cursor.execute(cls._SELECT)
                registros = cursor.fetchall();
                personas = [];
                for r in registros:
                    p = Persona(r[0], r[1], r[2], r[3], r[4])
                    personas.append(r);

                return list(personas);
        except Exception as ex:
            log.error(ex);

    @classmethod
    def insertInto(cls, persona) :
        try:
            with CursorPool() as cursor:       
                valores = (persona.nombre, persona.apellido, persona.correoElectronico, persona.edad);
                # log.info(valores)
                cursor.execute(cls._INSERT, valores);

            log.info(f'Archivo insertado correctamente. {cursor.rowcount}');
        except Exception as ex:
            log.error(ex);

    @classmethod
    def update(cls, persona) :
        try:
            with CursorPool() as cursor:       
                valores = (persona.nombre, persona.apellido, persona.correoElectronico, persona.edad, persona.idPersona);
                cursor.execute(cls._UPDATE, valores);

            log.info(f'Archivo actualizado correctamente. {cursor.rowcount}');
        except Exception as ex:
            log.error(ex);

    @classmethod
    def delete(cls, persona) :
        try:
            with CursorPool() as cursor:       
                valores = (persona.idPersona,);
                cursor.execute(cls._DELETE, valores);

            log.info(f'Archivo eliminado correctamente. {cursor.rowcount}');
        except Exception as ex:
            log.error(ex);


if __name__ == '__main__':
    persona1 = Persona(None, "Alansillo","Fernandez", "alansillo.fernandez@gmail.com", 16);
    personaAct = PersonaDao.insertInto(persona1);
    # log.info(type(persona1.edad))
    persona1 = Persona(1, "Alansillo2","Fernandez", "alansillo.fernandez@gmail.com", 16);
    # PersonaDao.update(persona1)

    persona3=Persona(idPersona=1)
    PersonaDao.delete(persona3)

     
     