class Persona:
    def __init__(self = None, nombre = None, apellido = None, edad = None, correoElectronico = None) -> None:
        self.nombre = nombre;
        self.apellido = apellido;
        self.edad = edad;
        self.correoElectronico = correoElectronico;
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}, {self.edad} años - {self.correoElectronico}.";
