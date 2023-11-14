class Usuario:
    def __init__(self, nombre,saldo_inicial = 0):
        self.nombre = nombre
        self.saldo = saldo_inicial
    def hacer_deposito(self, amount):
            self.saldo += amount
            print(f"Se hizo un deposito de {amount} .")
            return self
    def hacer_retiro(self, cantidad) :
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se retiro la suma de  {cantidad} .")
            else:
                print("Fondos insuficientes. No se pudo realizar el retiro.")
            return self
    def mostrar_balance_usuario(self):
                print(f"Saldo actual de {self.nombre}: {self.saldo}")
                return self

usuario_1= Usuario("usuario_1")
usuario_2=Usuario("usuario_2")
usuario_3=Usuario("usuario_3")

usuario_1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(500).hacer_retiro(100).mostrar_balance_usuario()
usuario_2.hacer_deposito(500).hacer_deposito(600).hacer_retiro(100).hacer_retiro(150).mostrar_balance_usuario()
usuario_3.hacer_deposito(400).hacer_retiro(50).hacer_retiro(20).hacer_retiro(200).mostrar_balance_usuario()
