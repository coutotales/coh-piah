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

    as_b = [wal, ttr, hlr, sal, sac, pal]
    
    return as_b

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

def n_palavras_unicas(lista_palavras): # SÓ funciona com LISTA [] de palavras '' #
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

def n_palavras_diferentes(lista_palavras): # SÓ funciona com LISTA [] de palavras '' #
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    soma_frases = 0
    soma_caracteres_frase = 0
    soma_caracteres_sentenca = 0
    soma_caracteres_palavras = 0
    lista_palavras = []
    for sentenca in sentencas:
        soma_frases = soma_frases + len(separa_frases(sentenca))
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        for frase in separa_frases(sentenca):
            soma_caracteres_frase = soma_caracteres_frase + len(frase)
            for palavra in separa_palavras(frase):
                lista_palavras.append(palavra)
                soma_caracteres_palavras = soma_caracteres_palavras + len(palavra)                
    wal = soma_caracteres_palavras / len(separa_palavras(texto))
    ttr = n_palavras_diferentes(lista_palavras) / len(separa_palavras(texto))
    hlr = n_palavras_unicas(lista_palavras) / len(separa_palavras(texto))
    sal = soma_caracteres_sentenca / len(sentencas)
    sac = soma_frases / len(sentencas)
    pal = soma_caracteres_frase / soma_frases

    as_a = [wal, ttr, hlr, sal, sac, pal]
    
    return as_a



def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe 2 ass e deve devolver o grau d similaridade nas ass.'''
    somatorio_dif = 0
    i = 0
    while i <= 5:
        somatorio_dif = somatorio_dif + abs(as_a[i] - as_b[i])
        i += 1
    similaridade_ab = somatorio_dif / 6

    return similaridade_ab

####TESTE####

texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
print(calcula_assinatura(texto))
print('')
print('R: [5.571, 0.825, 0.698, 210.0, 4.5, 45.888]')

    
