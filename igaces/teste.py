from sys import argv
from random import choice, randrange, random, randint, choices
from math import log
from time import sleep
from collections import defaultdict

import matplotlib.pyplot as plt

def shannon_entropy(cadeia_bits):
    entropia = 0

    for bit in '10':
        probabilidade = cadeia_bits.count(bit) / len(cadeia_bits)
        entropia += -probabilidade * log(probabilidade, 2)

    return entropia

def gerar_chave_artigo(n_iteracoes=1):
    PRIMOS = [
         2,  3,  5,  7,
        11, 13, 17, 19,
        23, 29, 31, 37,
        41, 43, 47, 53,
        59, 61, 67, 71,
        83, 89, 97
    ]

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

    # passos 13, 14, 15: refazer o processo até encontrar uma cadeia de bits
    # com entropia >= 95%
    entropia = shannon_entropy(bits_finais)

    if entropia >= 0.95:
        return bits_finais, entropia, n_iteracoes

    return gerar_chave_artigo(n_iteracoes+1)

def gerar_chave_basico(n_iteracoes=1):
    bits = ''.join(choices('10', k=64))
    entropia = shannon_entropy(bits)

    if entropia >= 0.95:
        return bits, entropia, n_iteracoes

    return gerar_chave_basico(n_iteracoes+1)

def simular(f, n):
    historico = defaultdict(int)

    for i in range(n):
        _, _, n_iteracoes = f()
        historico[n_iteracoes] += 1

    x = []
    y = []

    for n_iteracoes, vezes in sorted(historico.items()):
        x.append(n_iteracoes)
        y.append(vezes / n * 100)

    return x, y

def main():
    if len(argv) == 2:
        n = int(argv[1])
    else:
        n = 1000

    _, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

    ax1.set_ylim(ymin=0, ymax=100)
    ax2.set_ylim(ymin=0, ymax=100)

    ax1.set_title('Algoritmo proposto')
    x, y = simular(gerar_chave_artigo, n)
    ax1.bar(x, y)

    ax2.set_title('Algoritmo básico')
    x, y = simular(gerar_chave_basico, n)
    ax2.bar(x, y)

    plt.xlabel('Iterações necessárias')
    plt.ylabel('%% das ocorrências')

    plt.tight_layout()

    plt.show()

if __name__ == '__main__':
    main()

