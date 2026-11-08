def analisar_desempenho(notas):


    melhor_nota = max(notas)
    pior_nota = min(notas)
    media = sum(notas) / len(notas)

    if media >= 6.0:
        situacao = "aprovado"
    else:
        situacao = "reprovado"

    return {
        "maior_nota": melhor_nota,
        "menor_nota": pior_nota,
        "media_aritmetica": media,
        "situacao": situacao
    }

resultado = analisar_desempenho([8, 7, 9, 6])

print(resultado)
     

