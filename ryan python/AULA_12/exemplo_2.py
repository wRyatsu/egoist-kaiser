class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        

    def aumentar_salario(self, percentual):
        self.salario += self.salario * (percentual / 100)

class gerente(funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento


    def detalhes_gerente(self):
        return f"Gerante: {self.nome}, Salario: {self.salario}. Departamento: {self.departamento}"