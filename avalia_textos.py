def le_textos(): # O texto deve ser inserido SEM ASPAS #
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''    
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''


    #recebe: lista_de_textos = []    # função le_textos -> gera uma lista [] de textos
    #recebe: assinatura_ass_cp = [] # função le_assinatura _> gera uma lista [] assinatura


    #calcular assinatura para cada texto da lista_de_textos # função calcula_assinatura -> gera uma lista/ass [] para cada texto
    #comparar cada assinatura com a assinatura_ass_cp #função compara_assinatura -> gera o grau de similaridade para cada dupla

    #a que tiver menor similaridade_ab, deve ser a ecolhida. Apontar o 'i' correspondente


    
    textos = le_textos()
    ass_cp = le_assinatura()
    assinaturas = []
    similaridades = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)   # calculando a assinatura de cada texto dentro de 'textos'
        assinaturas.append(assinatura)    # inserindo cada assinatura na lista de assinaturas
        

    for assinatura in assinaturas:
        similaridade = compara_assinatura(assinatura, ass_cp)
        similaridades.append(similaridade)


    return similaridades





  

