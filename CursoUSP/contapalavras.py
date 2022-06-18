def qtd_de_palavras(palavrasAux):

    qtd = []
    i = 1
    qtdAux = []
    j = 0
    for linha in palavrasAux:
        print("Qtde de palavras da", i, "°", "senteça:", len(linha))
        qtd.append(len(linha))
        print()
        qtdAux = qtd
        
    print(qtdAux)
    return qtd

palavrasAux = [['Tamanho', 'médio', 'de', 'palavra:', 'Média', 'simples', 'do', 'número', 'de', 'caracteres', 'por', 'palavra.'], ['Tamanho', 'médio', 'de', 'palavra:', 'Média', 'simples', 'do', 'número', 'de', 'caracteres', 'por', 'palavra.Tamanho', 'médio', 'de', 'palavra:', 'Média', 'simples', 'do', 'número', 'de', 'caracteres', 'por', 'palavra.']]
qtd_de_palavras(palavrasAux)
