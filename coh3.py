import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +
                      " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    pass


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    pass


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    pass


def func_le_imprime_textos(textos):
    for i in range(len(textos)):
        print("o texto", i+1, " é:", textos[i])
    print()


def func_le_imprime_sentecas(textos):
    separaSentAux = []
    for i_do_texto in range(len(textos)):
        separaSentAux.append(separa_sentencas(textos[i_do_texto]))

    i = 1
    while i > 0:
        for i_da_sentenca in separaSentAux:
            print("Sentenças do", i, "°", "texto:", [i_da_sentenca])
            i = i + 1
            print()
        break
    return separaSentAux


def func_separa_frases(separaSentAux):
    separaFraseAux = []
    frasesAux = []
    for j in range(len(separaSentAux)):
        separaFraseAux.append(separaSentAux[j])

    for k in range(len(separaFraseAux)):
        frasesAux.append(separa_frases(separaFraseAux[k]))

    i = 1
    while i > 0:
        for i_da_sentenca in frasesAux:
            print("Frases da", i, "°", "senteça:", [i_da_sentenca])
            i = i + 1
            print()
        break

    return frasesAux


def func_separa_palavras(frasesAux):
    palavrasAux = []
    separaPalavrasAux = []
    for l in range(len(frasesAux)):
        separaPalavrasAux.append(frasesAux[l])

    for m in range(len(separaPalavrasAux)):
        palavrasAux.append(separa_palavras(separaPalavrasAux[m]))

    i = 1
    while i > 0:
        for i_da_sentenca in palavrasAux:
            print("Palavras da", i, "°", "senteça:", [i_da_sentenca])
            i = i + 1
            print()
        break

    return palavrasAux


def func_tamanho_medio_palavra(palavrasAux):
    # Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
    def imprimir_lista(lista):
        for elemento in lista:
            if isinstance(elemento, list):  # se este elemento é uma lista, chama a mesma funçao
                imprimir_lista(elemento)
            else:  # caso contrário imprime normalmente
                print(elemento)
    imprimir_lista(palavrasAux)


def main():
    texto = le_textos()
    separaSentencas = (texto)
    separaFrases = (separaSentencas)
    separaPalavras = (separaFrases)
    #somaPalavras = func_tamanho_medio_palavra(separaPalavras)

    func_le_imprime_textos(texto)
    func_le_imprime_sentecas(texto)
    func_separa_frases(separaSentencas)
    func_separa_palavras(separaFrases)
    func_tamanho_medio_palavra(separaPalavras)


main()
