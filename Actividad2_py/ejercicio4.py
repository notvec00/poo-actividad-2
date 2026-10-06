import math


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return math.pi * 2 * self.radio


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return math.pow(self.lado, 2)

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura / 2

    def calcular_perimetro(self):
        return self.base + self.altura + math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def determinar_tipo_triangulo(self):
        if self.base == self.altura and self.base == self.calcular_hipotenusa() and self.altura == self.calcular_hipotenusa():
            print('Es triangulo equilatero')
        elif self.base != self.altura and self.base != self.calcular_hipotenusa() and self.altura != self.calcular_hipotenusa():
            print('Es un triangulo escaleno')
        else:
            print('Es un triangulo isosceles')


def main():
    circulo = Circulo(2)
    print(f'El área del círculo es: {circulo.calcular_area()}')
    print(f'El perímetro del círculo es: {circulo.calcular_perimetro()}')

    rectangulo = Rectangulo(1, 2)
    print(f'El área del rectángulo es: {rectangulo.calcular_area()}')
    print(f'El perímetro del rectángulo es: {rectangulo.calcular_perimetro()}')

    cuadrado = Cuadrado(3)
    print(f'El área del cuadrado es: {cuadrado.calcular_area()}')
    print(f'El perímetro del cuadrado es: {cuadrado.calcular_perimetro()}')

    triangulo = TrianguloRectangulo(3, 5)
    print(f'El área del triángulo es: {triangulo.calcular_area()}')
    print(f'El perímetro del triángulo es: {triangulo.calcular_perimetro()}')
    print(f'La hipotenusa del triángulo es: {triangulo.calcular_hipotenusa()}')
    triangulo.determinar_tipo_triangulo()


if __name__ == "__main__":
    main()
