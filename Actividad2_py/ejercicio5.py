from enum import Enum


class TipoCuenta(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"


class CuentaBancaria:
    def __init__(self, nombres_titular, apellidos_titular, numero_cuenta, tipo_cuenta):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0

    def imprimir(self):
        print(f'Nombres del titular = {self.nombres_titular}')
        print(f'Apellidos del titular = {self.apellidos_titular}')
        print(f'Número de cuenta = {self.numero_cuenta}')
        print(f'Tipo de cuenta = {self.tipo_cuenta.name}')
        print(f'Saldo = {self.saldo}')

    def consultar_saldo(self):
        print(f'El saldo de la cuenta es ${self.saldo}')

    def consignar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}')
            return True
        print('El valor a consignar debe ser mayor que 0')
        return False

    def retirar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}')
            return True
        print('No es posible retirar ese valor')
        return False

    def comparar_cuentas(self, cuenta):
        if self.saldo > cuenta.saldo:
            print(f'La cuenta de {self.nombres_titular} tiene mayor saldo que la de {cuenta.nombres_titular}')
        elif self.saldo < cuenta.saldo:
            print(f'La cuenta de {self.nombres_titular} tiene menor saldo que la de {cuenta.nombres_titular}')
        else:
            print('Las dos cuentas tienen el mismo saldo')

    def transferencia(self, cuenta, valor):
        if self.retirar(valor):
            cuenta.consignar(valor)


def main():
    cuenta = CuentaBancaria('Pedro', 'Pérez', 123456789, TipoCuenta.AHORROS)
    cuenta.imprimir()
    cuenta.consignar(200000)
    cuenta.consignar(300000)
    cuenta.retirar(400000)

    cuenta2 = CuentaBancaria('Ana', 'Gómez', 987654321, TipoCuenta.CORRIENTE)
    cuenta.comparar_cuentas(cuenta2)
    cuenta.transferencia(cuenta2, 50000)
    cuenta2.consultar_saldo()


if __name__ == "__main__":
    main()
