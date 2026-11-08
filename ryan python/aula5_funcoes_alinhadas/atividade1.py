cliente = str(input("Que Tipo De Cliente Você é?(VIP, Padrao ou Outro?)"))
valor_gasto = float(input("Quanto Você Gastou no total?"))

if cliente == "VIP":
    valor_gasto = valor_gasto - valor_gasto * 0.20
    print(f"O valor com desconto aplicado é de {valor_gasto}") 
elif cliente == "Padrao":
        valor_gasto >= 200
        valor_gasto = valor_gasto - valor_gasto * 0.10
        print(f"O valor com desconto aplicado é de {valor_gasto}")
else:
        print("Você nâo tem direito a desconto")








