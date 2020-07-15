class Node:
    def __init__(self, val):
        self.item = val
        self.next = None

class LinkedList:
    def __init__(self):
      self.head = None

#funcao para adicionar nodo ao final
    def addNode(self, val):
      new_node = Node(val)
      if self.head is None:
        self.head = new_node
        return
      n = self.head
      while n.next is not None:
        n= n.next
      n.next = new_node;

#busca sequencial
    def buscaseq(self, x):
        if self.head is None:
          print("Lista vazia!")
          return
        n = self.head
        while n is not None:
          if n.item == x:
            print("Elemento {} está presente no arranjo.".format(x))
            return True
          n = n.next
        print("Elemento {} não está presente no arranjo.".format(x))
        return False

#imprime a lista
    def printlnklist(self):
      printval = self.head
      while printval is not None:
        print (printval.item)
        printval = printval.next

#cria arranjo
listarr = LinkedList()
for i in range(100000):
    listarr.addNode(i)

#verifica a lista criada - imprime lista
listarr.printlnklist()

#incio dos testes
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
arrbusca = arranjo100k
ultimo = ult100k

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
listarr.buscaseq(0)
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
listarr.buscaseq(ultimo)
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
listarr.buscaseq(-1)
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
    #utiliza o mesmo seed para o conjunto
    random.seed(ctrl)
    #valor para busca aleatória
    num = random.choice(arrbusca)
    #mede tempo inicial
    t0 = time.time_ns()
    #efetua a busca
    listarr.buscaseq(num)
    #mede tempo final
    t1 = time.time_ns()
    #calculo do tempo decorrido
    print("Tempo: ", t1 - t0)
    ctrl = ctrl+1
