import Rectangulo as Figura;

miRectangulo = Figura.Rectangulo(15, 55);

print(miRectangulo.calcularArea());

miRectangulo._ancho = 1;
miRectangulo._largo = 2;

print(miRectangulo.calcularArea());

miRectangulo.Ancho = 10;
miRectangulo.color = "Azul";

print(miRectangulo.calcularArea());
print(miRectangulo.color)
