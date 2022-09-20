from random import shuffle
import time

def insertion_sort(lista):

    for i in range(1, len(lista)):
        chave = lista[i]
        k = i
        while k > 0 and chave < lista[k - 1]:
            lista[k] = lista[k - 1]
            k -= 1
        lista[k] = chave


def mergeSort(lista):

    if len(lista) > 1:

        meio = len(lista)//2
        #também é valido: meio = int(len(lista)/2)

        listaDaEsquerda = lista[:meio]
        listaDaDireita = lista[meio:]

        mergeSort(listaDaEsquerda)
        mergeSort(listaDaDireita)

        i = 0
        j = 0
        k = 0

        while i < len(listaDaEsquerda) and j < len(listaDaDireita):

            if listaDaEsquerda[i] < listaDaDireita[j]:
                lista[k]=listaDaEsquerda[i]
                i += 1
            else:
                lista[k]=listaDaDireita[j]
                j += 1
            k += 1

        while i < len(listaDaEsquerda):

            lista[k]=listaDaEsquerda[i]
            i += 1
            k += 1

        while j < len(listaDaDireita):
            lista[k]=listaDaDireita[j]
            j += 1
            k += 1
    return lista


MAX_CHARS = 10


def numero_do_balde(palavra, pos):
    if pos > len(str(palavra)) -1:
        return 0
    ch = palavra
    #pegar caractere
    for i in range(pos):
        ch = ch//10

    return ch%10

def radix_sort(lista):
        tamanho_maximo = len(str(max(lista)))

        for pos in range(0, tamanho_maximo):
                baldes = [list() for y in range(MAX_CHARS)]
                for palavra in lista:
                        balde = numero_do_balde(palavra, pos)
                        baldes[balde] += [palavra]
                lista = sum(baldes, [])

        return lista


for tamanhoDaInstancia in [100, 1_000, 10_000, 100_000, 1_000_000]:
    with open("resultados"+str(tamanhoDaInstancia)+".txt", "w") as arquivo:
        for i in range(20):
            vetorNaoOrdenado = list(range(tamanhoDaInstancia))
            shuffle(vetorNaoOrdenado)

            algoritmoA = vetorNaoOrdenado.copy()
            algoritmoB = vetorNaoOrdenado.copy()
            algoritmoC = vetorNaoOrdenado.copy()

            tempoInicial = time.time()
            insertion_sort(algoritmoA)
            arquivo.write(str(time.time()-tempoInicial) + " ")

            tempoInicial = time.time()
            mergeSort(algoritmoB)
            arquivo.write(str(time.time() - tempoInicial) + " ")

            tempoInicial = time.time()
            radix_sort(algoritmoC)
            arquivo.write(str(time.time() - tempoInicial) + " ")

            arquivo.write("\n")
