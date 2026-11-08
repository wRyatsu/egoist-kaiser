class NomeDaClasse:
    def __init__(self, parametro1, parametro2):
        self.atributo1 = parametro1
        self.atributo2 = parametro2
    
    def metodo_exemplo(self):
        return f"Atributo 1: {self.atributo1}, atributo 2: {self.atributo2}"
    

p1 = NomeDaClasse("joao", 30)

print(p1.metodo_exemplo())
