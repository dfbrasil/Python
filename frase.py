import re

lista = []


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


lista = separa_frases("Assim, são presentes, nos textos de caráter narrativo, personagens principais e secundários, e espaço(s) e tempo(s). O espaço pode referir-se a espaços físicos (como um país, estado, cidade) ou sociais (como as elites, as classes populares, os intelectuais etc.).")

print(lista)
