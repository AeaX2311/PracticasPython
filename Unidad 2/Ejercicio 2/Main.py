import PersonaDao as dao

persona1 = dao.persona.Persona("Alansillo","Fernandez", 16, "alansillo.fernandez@gmail.com");
print(persona1)

print(dao.selectAllPersona())