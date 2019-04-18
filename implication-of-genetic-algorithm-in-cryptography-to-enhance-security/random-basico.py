from random import choices
from math import log

def shannon_entropy(cadeia_bits):
    entropia = 0

    for bit in '10':
        probabilidade = cadeia_bits.count(bit) / len(cadeia_bits)
        entropia += -probabilidade * log(probabilidade, 2)

    return entropia

def gerar_chave(counter=1):
    bits = ''.join(choices('10', k=64))
    entropia = shannon_entropy(bits)

    if entropia >= 0.95:
        return bits, entropia, counter

    return gerar_chave(counter+1)

chave, entropia, counter = gerar_chave()

print('Chave:', chave)
print('Tamanho da chave:', len(chave), 'bits')
print('Entropia:', entropia)
print('# de iterações para gerar a chave:', counter)
