from random import choice, randrange, random
from math import log
from time import sleep

QUANTIDADE_CROMOSOMOS_INDIVIDUO = 17
QUANTIDADE_POPULACAO = 1000
TAXA_MUTACAO = 50 / 100

BYTES = range(256)

def calcular_entropia(cadeia_bytes):
    entropia = 0

    for byte in BYTES:
        p_x = cadeia_bytes.count(byte) / len(cadeia_bytes)

        if p_x > 0:
            entropia += -p_x * log(p_x, 256)

    return entropia

class Individuo():
    def __init__(self, cromossomos):
        self.cromossomos = cromossomos
        self.entropia = calcular_entropia([c.byte for c in cromossomos])

    def __repr__(self):
        return f'Individuo({self.cromossomos})'

    def __str__(self):
        return ' '.join(map(str, self.cromossomos))

class Cromossomo():
    def __init__(self, byte=None):
        if byte == None:
            byte = randrange(256)

        self.bits = format(byte, 'b').rjust(8, '0')
        self.byte = byte

    def __repr__(self):
        return f'Cromossomo({self.byte})'

    def __str__(self):
        return self.bits

def criar_populacao_aleatoria():
    populacao = []

    for _ in range(QUANTIDADE_POPULACAO):
        cromossomos = [Cromossomo() for _ in range(QUANTIDADE_CROMOSOMOS_INDIVIDUO)]
        individuo = Individuo(cromossomos)
        populacao.append(individuo)

    return sorted(populacao, key=lambda x: x.entropia, reverse=True)

def gerar_proxima_populacao(populacao):
    proxima_populacao = []

    melhores = populacao[:(int(QUANTIDADE_POPULACAO * 0.2))]

    for _ in range(QUANTIDADE_POPULACAO):
        individuo1 = choice(melhores)
        individuo2 = choice(populacao)

        corte = randrange(QUANTIDADE_CROMOSOMOS_INDIVIDUO)

        cromossomos_selecionados = []

        for i in range(QUANTIDADE_CROMOSOMOS_INDIVIDUO):
            if i < corte:
                cromossomos_selecionados.append(individuo1.cromossomos[i])
            else:
                cromossomos_selecionados.append(individuo2.cromossomos[i])

            if random() < TAXA_MUTACAO:
                cromossomos_selecionados[i] = Cromossomo()

        proxima_populacao.append(Individuo(cromossomos_selecionados))

    return sorted(populacao, key=lambda x: x.entropia, reverse=True)

def main():
    print(f'QUANTIDADE_CROMOSOMOS_INDIVIDUO = {QUANTIDADE_CROMOSOMOS_INDIVIDUO}')
    print(f'QUANTIDADE_POPULACAO = {QUANTIDADE_POPULACAO}')
    print(f'TAXA_MUTACAO = {TAXA_MUTACAO}')
    print()
    print('Ctrl+C para encerrar a simulação')
    print()
    print('A simulação começará em 5 segundos...')
    print()

    sleep(5)

    populacao = criar_populacao_aleatoria()

    print(f'Melhor entropia na geração inicial: {populacao[0].entropia}')

    geracao = 1

    while True:
        if geracao % 10 == 0:
            print(f'Melhor entropia na geração {geracao}: {populacao[0].entropia}')

        populacao = gerar_proxima_populacao(populacao)
        geracao += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
