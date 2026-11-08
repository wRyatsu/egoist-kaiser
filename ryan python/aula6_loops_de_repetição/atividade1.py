
acesso = "admin123"
# senha
contador = 3
# número de tentativas

while contador > 0:
    dados = input("Qual é a senha de acesso? ")
# perguntar pela senha
    if dados == acesso:
        # comparar valores
        print("Acesso Permitido")
        break
    else:
        contador -= 1
        # caso a senha esteja incorreta
        print("Senha Incorreta")


        if contador > 0:
            print(f"Restam {contador} Tentativas")
            # numero restante de tentativas
        else:
            print("Acesso Negado")

    
