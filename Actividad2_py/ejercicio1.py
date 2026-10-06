class Persona:
    def __init__(self, nombre, apellidos, id, yob):
        self.nombre = nombre
        self.apellidos = apellidos
        self.id = id
        self.yob = yob

    def imprimir(self):
        print(f'Nombre = {self.nombre}\nApellidos = {self.apellidos}\nNumero de documento de identidad = {self.id}\nAno de nacimiento = {self.yob}')


def main():
    p1 = Persona('Rochi', 'Roldan Laverde', 1010104101, 2005)
    p1.imprimir()

    p2 = Persona('Zype', 'Monsalve Mazo', 1089893799, 2003)
    p2.imprimir()


if __name__ == "__main__":
    main()
