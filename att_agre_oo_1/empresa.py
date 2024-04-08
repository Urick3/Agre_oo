from funcionario import Funcionario

class Empresa:
    def __init__(self, nome, funcionarios=None):
        self.nome = nome
        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def contratar(self, funcionario):

        self.funcionarios.append(funcionario)
    
    def exibir_funcionarios(self):
        for funcionario in self.funcionarios:
         print(funcionario)
                                 