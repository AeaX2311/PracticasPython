from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color) :
    def __init__(self, ancho, largo) -> None:
        self._ancho = ancho;
        self._largo = largo;

    @property
    def Ancho(self) :
        return self._ancho;
    @Ancho.setter
    def Ancho(self, ancho) :
        self._ancho = ancho;
    
    def calcularArea(self) :
        return self._ancho * self._largo;

