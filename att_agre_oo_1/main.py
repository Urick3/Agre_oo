from funcionario import Funcionario
from empresa import Empresa 

def main():
    funcionario1 = Funcionario("Júlio", 2500.0)
    funcionario2 = Funcionario("Eduarda", 3500.0)
    funcionario3 = Funcionario("Rodrigo", 3200.0)

    empresa = Empresa("TechCorp",[funcionario1, funcionario2])
    empresa.contratar(funcionario3)

    print(f"Funcionarios da empresa{empresa.nome}:")
    empresa.exibir_funcionarios()

if __name__ == "__main__":
    main()