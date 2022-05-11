
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

# PASSO 1

# IMPLEMENTAR

# Tamanho médio de palavra: Média simples do número de caracteres por palavra.


def main():
    textosAux = []
    textosAux = le_textos()
    separaSentAux = []
    separaFraseAux = []
    frasesAux = []
    palavrasAux = []
    separaPalavrasAux = []

    for i in range(len(textosAux)):
        print("o texto", i+1, " é:", textosAux[i])
        print()

    for i_do_texto in range(len(textosAux)):
        separaSentAux.append(separa_sentencas(textosAux[i_do_texto]))

    i = 1
    while i > 0:
        for i_da_sentenca in separaSentAux:
            print("sentenças da", i, "°", "frase", [i_da_sentenca])
            i = i + 1
            print()
        break

    for j in range(len(separaSentAux)):
        separaFraseAux.append(','.join(separaSentAux[j]))

    for k in range(len(separaFraseAux)):
        frasesAux.append(separa_frases(separaFraseAux[k]))

    for l in range(len(frasesAux)):
        separaPalavrasAux.append(','.join(frasesAux[l]))

    for m in range(len(separaPalavrasAux)):
        palavrasAux.append(separa_palavras(separaPalavrasAux[m]))

    print(palavrasAux)

 # Tamanho médio das palavras
# Soma dos tamanhos das palavras / nº de palavras


def tamanho_medio_das_palavras(palavrasAux):
    print(palavrasAux)


main()

""" arrays = [['3 -1 2 0 2 0 -1 -1', '4 2 4 5 1 0 0 1 1'], ['6 -8 -8 15 15 0', '5 -1 3 2']]

newArrays = list()
temp = list()

for array in arrays:
    for item in array:
        temp.append([item])

    newArrays.append(temp.copy())
    temp.clear()
    
print(newArrays) """
