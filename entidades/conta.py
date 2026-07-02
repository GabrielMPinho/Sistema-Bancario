from entidades.cliente import Cliente

class Conta:
    def __init__(self, id, cliente: Cliente, tipo):
        self.id = id
        self.cliente = cliente
        self.tipo = tipo
        self.saldo = 0

    def __str__(self):
        return f"Id da conta: {self.id}\nDono da conta: {self.cliente}\nTipo da conta: {self.tipo}\nSaldo atual: {self.saldo}\n"