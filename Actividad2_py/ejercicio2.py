from enum import Enum


class TipoPlaneta(Enum):
    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"


class Planeta:
    def __init__(self, nombre=None, satelites=0, masa=0, volumen=0, diametro=0, dsol=0, tipo=None, observable=False):
        self.nombre = nombre
        self.satelites = satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.dsol = dsol
        self.tipo = tipo
        self.observable = observable

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.dsol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.observable}")

    def densidad(self):
        return self.masa / self.volumen if self.volumen != 0 else 0

    def planetaExterior(self):
        limite = 508632758
        return self.dsol > limite


def main():
    marte = Planeta('Tierra', 1, 5.9736E24, 1.08321E12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
    marte.imprimir()
    print(f'Es exterior = {marte.planetaExterior()}')
    print(f'Densidad = {marte.densidad()}')

    jupiter = Planeta('Jupiter', 79, 1.899E27, 1.4313E15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
    jupiter.imprimir()
    print(f'Es exterior = {jupiter.planetaExterior()}')
    print(f'Densidad = {jupiter.densidad()}')


if __name__ == "__main__":
    main()
