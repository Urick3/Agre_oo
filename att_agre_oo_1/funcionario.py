class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def __str__(self):
        return f"Nome:{self.nome}, salário: {self.salario}"