def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe 2 ass e deve devolver o grau d similaridade nas ass.'''
    somatorio_dif = 0
    i = 0
    while i <= 5:
        somatorio_dif = somatorio_dif + abs(as_a[i] - as_b[i])
        i += 1
    similaridade_ab = somatorio_dif / 6

    return similaridade_ab


####TESTES####

print(compara_assinatura([5.571, 0.825, 0.698, 210.0, 4.5, 45.888], [5.571428571428571, 0.8253968253968254, 0.6984126984126984, 210.0, 4.5, 45.888888888888886]))
