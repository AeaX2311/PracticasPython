class Persona:
    def __init__(self = None, idPersona = None, nombre = None, apellido = None, correoElectronico = None, edad = None):
        self.idPersona = idPersona;
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = int(edad);
        self.correoElectronico = correoElectronico;
    
    def __str__(self) -> str:
        return f"[{self.idPersona}] - {self.nombre} {self.apellido}, {self.edad} años - {self.correoElectronico}.";
