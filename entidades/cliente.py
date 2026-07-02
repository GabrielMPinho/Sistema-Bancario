class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.conta = None
        self.cpf = cpf
    
    def __str__(self):
        return f"\n    Nome: {self.nome}\n    CPF: {self.cpf}\n"















































