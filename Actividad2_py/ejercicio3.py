from enum import Enum


class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"


class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"


class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"


class Automovil:
    def __init__(self, marca, modelo, motor, tipo_combustible, tipo_automovil, numero_puertas, cantidad_asientos, velocidad_maxima, color, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = velocidad_actual

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor

    def getTipoCombustible(self):
        return self.tipo_combustible

    def getTipoAutomovil(self):
        return self.tipo_automovil

    def getNumeroPuertas(self):
        return self.numero_puertas

    def getCantidadAsientos(self):
        return self.cantidad_asientos

    def getVelocidadMaxima(self):
        return self.velocidad_maxima

    def getColor(self):
        return self.color

    def getVelocidadActual(self):
        return self.velocidad_actual

    def setMarca(self, marca):
        self.marca = marca

    def setModelo(self, modelo):
        self.modelo = modelo

    def setMotor(self, motor):
        self.motor = motor

    def setTipoCombustible(self, tipo_combustible):
        self.tipo_combustible = tipo_combustible

    def setTipoAutomovil(self, tipo_automovil):
        self.tipo_automovil = tipo_automovil

    def setNumeroPuertas(self, numero_puertas):
        self.numero_puertas = numero_puertas

    def setCantidadAsientos(self, cantidad_asientos):
        self.cantidad_asientos = cantidad_asientos

    def setVelocidadMaxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def setColor(self, color):
        self.color = color

    def setVelocidadActual(self, velocidad_actual):
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento_velocidad):
        if incremento_velocidad + self.velocidad_actual <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            print(f'No es posible acelerar a mas de {self.velocidad_maxima}')

    def desacelerar(self, disminucion_velocidad):
        if self.velocidad_actual - disminucion_velocidad >= 0:
            self.velocidad_actual -= disminucion_velocidad
        else:
            print(f'No es posible desacelerar a menos de 0')

    def frenar(self):
        self.setVelocidadActual(0)

    def calcular_tiempo_llegada(self, distancia):
        return distancia / self.velocidad_actual if self.velocidad_actual != 0 else None

    def imprimir(self):
        print(f'Marca = {self.marca}')
        print(f'Modelo = {self.modelo}')
        print(f'Motor = {self.motor}')
        print(f'Tipo de combustible = {self.tipo_combustible.name}')
        print(f'Tipo de automovil = {self.tipo_automovil.name}')
        print(f'Numero de puertas = {self.numero_puertas}')
        print(f'Cantidad de asientos = {self.cantidad_asientos}')
        print(f'Velocidad maxima = {self.velocidad_maxima}')
        print(f'Color = {self.color.name}')
        print(f'Velocidad actual = {self.velocidad_actual}')


def main():
    marcherati = Automovil('Nissan', 2023, 1600, TipoCom.GAS_NATURAL, TipoA.EJECUTIVO, 5, 5, 320, TipoColor.BLANCO, 100)
    marcherati.imprimir()
    marcherati.acelerar(20)
    print(marcherati.getVelocidadActual())
    marcherati.desacelerar(50)
    print(marcherati.getVelocidadActual())
    marcherati.frenar()
    print(marcherati.getVelocidadActual())


if __name__ == "__main__":
    main()
