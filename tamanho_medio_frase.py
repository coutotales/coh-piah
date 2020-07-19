import re

def separa_sentencas(texto): # O texto deve ser inserido ENTRE ASPAS #
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca): # Deve reveber UMA sentença ENTRE ASPAS #
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase): # Funciona com texto, sentença ou frase ENTRE '' #
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def tamanho_medio_frase(texto):
    sentencas = separa_sentencas(texto)
    soma_frases = 0
    soma_caracteres = 0
    for sentenca in sentencas:
        soma_frases = soma_frases + len(separa_frases(sentenca))
        for frase in separa_frases(sentenca):
            soma_caracteres = soma_caracteres + len(frase)

    tamanho_med = soma_caracteres / soma_frases

    complexidade_sentenca = soma_frases / len(sentencas)


    return complexidade_sentenca, tamanho_med

    
