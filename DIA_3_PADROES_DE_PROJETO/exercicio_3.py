from abc import ABC, abstractclassmethod


class Grafico(ABC):
    @abstractclassmethod
    def area(self):
        raise NotImplementedError

    def perimetro(self):
        raise NotImplementedError


class Quadrado(Grafico):
    def __init__(self, lado) -> None:
        super().__init__()
        self.lado = lado

    def area(self):
        return self.lado**2

    def perimetro(self):
        return self.lado * 4


class Retangulo(Grafico):
    def __init__(self, base, altura) -> None:
        super().__init__()
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


class Circulo(ABC):
    def __init__(self, raio) -> None:
        super().__init__()
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio**2)

    def perimetro(self):
        return 2 * (3.14 * self.raio)


quadrado = Quadrado(5)
retangulo = Retangulo(3, 6)
circulo = Circulo(8)
print(quadrado.area())
print(quadrado.perimetro())
print(retangulo.area())
print(retangulo.perimetro())
print(circulo.area())
print(circulo.perimetro())
