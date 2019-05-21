from sys import argv
from random import choice, randrange, random, randint, choices
from math import log
from time import sleep
from collections import defaultdict

def shannon_entropy(cadeia_bits):
    entropia = 0

    for bit in '10':
        probabilidade = cadeia_bits.count(bit) / len(cadeia_bits)
        entropia += -probabilidade * log(probabilidade, 2)

    return entropia

def gerar_chave_artigo(n_iteracoes=1):
    PRIMOS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
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
        return bits_finais, entropia, n_iteracoes

    return gerar_chave_artigo(n_iteracoes+1)

def gerar_chave_basico(n_iteracoes=1):
    bits = ''.join(choices('10', k=64))
    entropia = shannon_entropy(bits)

    if entropia >= 0.95:
        return bits, entropia, n_iteracoes

    return gerar_chave_basico(n_iteracoes+1)

def print_ajuda():
    print('2 Argumentos:')
    print('artigo|basico')
    print('# de iterações')
    
def main():
    if len(argv) != 3:
        print_ajuda()
        return
    
    if argv[1] == 'artigo':
        f = gerar_chave_artigo
    elif argv[1] == 'basico':
        f = gerar_chave_basico
    else:
        print_ajuda()
        return
    
    try:
        n = int(argv[2])
    except ValueError:
        print_ajuda()
        return
        
    historico = defaultdict(int)
    
    for i in range(n):
        chave, entropia, n_iteracoes = f()
        historico[n_iteracoes] += 1
        
    for n_iteracoes, vezes in sorted(historico.items()):
        porcentagem = vezes / n * 100
        print(f'{n_iteracoes} iteracoes: {porcentagem:5.2f}%')

if __name__ == '__main__':
    main()
    
