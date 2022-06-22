
from math import inf
from time import time

def meu_max(iteravel):
    numero_maximo = -inf
    for numero in iteravel:
        if numero > numero_maximo:
            numero_maximo = numero
    return numero_maximo


if __name__ == '__main__':
    print(meu_max([1]))
    print(meu_max([1,100]))

    print('Estudo experimental sobre o tempo da execucao da funcao max')

    print('testando para entrada de tamanho 2')
    inicio = time()
    meu_max(range(n))
    fim = time()
    tempo_de_execucao_em_segundos = fim - inicio
    print('*'* int(tempo_de_execucao_em_segundos * 10),n)
