from random import choice, randrange, random, randint, choices
from math import log
from time import sleep

PRIMOS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def shannon_entropy(cadeia_bits):
    entropia = 0

    for bit in '10':
        probabilidade = cadeia_bits.count(bit) / len(cadeia_bits)
        entropia += -probabilidade * log(probabilidade, 2)

    return entropia

def gerar_chave(counter=1):
    # passos 1, 2, 3: gerar um array aleatório com letras de A-Z
    array_caracteres = [randint(65, 91) for _ in range(16)]

    # passos 4, 5, 6: gerar um array aleatório com 16 números primos de 0-100
    array_primos = choices(PRIMOS, k=16)

    # passos 7, 8: gerar um array aleatório com 8 numeros de 1-7
    pontos_corte = [randint(1, 7) for _ in range(8)]

    # passos 9, 10: combinar os caracteres e os numeros primos
    populacao = []

    for corte in pontos_corte:
        x1 = array_caracteres.pop()
        x2 = array_primos.pop()

        x1 = format(x1, 'b').rjust(8, '0')
        x2 = format(x2, 'b').rjust(8, '0')

        individuo = x1[corte:] + x2[:corte]
        populacao.append(individuo)

    # passos 11, 12: aplicar mutação nos individuos gerados anteriormente
    bits_finais = ''
    for i in range(len(populacao)):
        primeiro_bit = '1' if populacao[i][0] == '0' else '0'
        ultimo_bit = '1' if populacao[i][7] == '0' else '0'
        bits_finais += primeiro_bit + populacao[i][1:7] + ultimo_bit


    # passos 13, 14, 15: refazer o processo até encontrar uma cadeia de bits com entropia >=95%
    entropia = shannon_entropy(bits_finais)

    if entropia >= 0.95:
        return bits_finais, entropia, counter

    return gerar_chave(counter+1)

chave, entropia, counter = gerar_chave()

print('Chave:', chave)
print('Tamanho da chave:', len(chave), 'bits')
print('Entropia:', entropia)
print('# de iterações para gerar a chave:', counter)
