def buscabin(arranjo, elemento_desejado):
    esquerda, direita = 0, len(arranjo) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arranjo[meio] == elemento_desejado:
            print("Elemento {} está presente no arranjo.".format(elemento_desejado))
            return meio
        elif arranjo[meio] > elemento_desejado:
            direita = meio - 1
        else: #ou seja, se arranjo[meio] < elemento_desejado
            esquerda = meio + 1
    print("Elemento {} não está presente no arranjo.".format(elemento_desejado))
    return -1
    
    
import time
import random
import sys

#variaveis auxiliares ult elemento dos arranjos
ult1k = 999
ult2k = 1999
ult5k = 4999
ult10k = 9999
ult100k = 99999

#define os arranjos de busca
arranjo1k = list(range(0, 1000))
arranjo2k = list(range(0, 2000))
arranjo5k = list(range(0, 5000))
arranjo10k = list(range(0, 10000))
arranjo100k = list(range(0, 100000))

#variaveis auxiliares para buscas
arrbusca = arranjo1k
ultimo = ult1k

#define saida em arquivo texto
#sys.stdout = open("results.txt", "w")

#variavel de controle do loop
ctrl = 0

#A- pesquisa 1o elemento
print("### TESTE nº ", (ctrl+1)," ###")
#variaveis de controle do tempo
t0=0
t1=0
#mede tempo inicial
t0 = time.time_ns()
#efetua a busca
buscabin(arrbusca, 0)
#mede tempo final
t1 = time.time_ns()
#calculo do tempo decorrido
print("Tempo: ", t1 - t0)
ctrl=ctrl+1

#A- pesquisa ult
print("### TESTE nº ", (ctrl+1)," ###")
#variaveis de controle do tempo
t0=0
t1=0
#mede tempo inicial
t0 = time.time_ns()
#efetua a busca
buscabin(arrbusca, ultimo)
#mede tempo final
t1 = time.time_ns()
#calculo do tempo decorrido
print("Tempo: ", t1 - t0)
ctrl=ctrl+1

#B- pesquisa não-existente
print("### TESTE nº ", (ctrl+1)," ###")
#variaveis de controle do tempo
t0=0
t1=0
#mede tempo inicial
t0 = time.time_ns()
#efetua a busca
buscabin(arrbusca, -1)
#mede tempo final
t1 = time.time_ns()
#calculo do tempo decorrido
print("Tempo: ", t1 - t0)
ctrl=ctrl+1

#loop de repetição para 100 buscas
while ctrl < 100:
    print("### TESTE nº ", (ctrl+1)," ###")
    #C- pesquisa existente aleatorio
    #variaveis de controle do tempo
    t0=0
    t1=0
    #valor para busca aleatória
    num = random.choice(arrbusca)
    #mede tempo inicial
    t0 = time.time_ns()
    #efetua a busca
    buscabin(arrbusca, num)
    #mede tempo final
    t1 = time.time_ns()
    #calculo do tempo decorrido
    print("Tempo: ", t1 - t0)
    ctrl = ctrl+1

#fecha arquivo texto
#sys.stdout.close()
