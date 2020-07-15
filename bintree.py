class Node(object):
    def __init__(self, val):
        self.leftnd = None
        self.rightnd = None
        self.val = val

class BinTree(object):
    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.rightnd = self.insert(root.rightnd, node)
        else:
            root.leftnd = self.insert(root.leftnd, node)
        return root

    def inorderPrint(self, root):
        if not root:
            return None
        else:
            self.inorderPrint(root.leftnd)
            print(root.val)
            self.inorderPrint(root.rightnd)

    def preorderPrint(self, root):
        if not root:
            return None
        else:
            print(root.val)
            self.preorderPrint(root.leftnd)
            self.preorderPrint(root.rightnd)

    def postorderPrint(self, root):
        if not root:
            return None
        else:
            self.postorderPrint(root.leftnd)
            self.postorderPrint(root.rightnd)
            print(root.val)

    def buscatree(self, root, key): 
        if root is None:
            print("{} Not found!".format(key))
            return
        if root.val == key: 
            print("{} Found!".format(root.val))
            return
        if root.val < key: 
            return self.buscatree(root.rightnd, key) 
        return self.buscatree(root.leftnd, key) 

#incio dos testes
import time
import random
import sys
sys.setrecursionlimit(10**7)
reclim = sys.getrecursionlimit()
print(reclim)

#variaveis auxiliares ult elemento dos arranjos
ult1k = 999
ult2k = 1999
ult5k = 5999

#define os arranjos de busca
#arranjo1k = list(range(0, 1000))
#arranjo2k = list(range(0, 2000))
#arranjo5k = list(range(0, 6000))

node = BinTree()
#arranjo = arranjo5k
#popula arvore
raiz = Node(ult5k//2) #raiz valor inteiro de n/2
#for nd in arranjo:
nd = 0
while nd <= ult5k:
    node.insert(raiz, Node(nd))
    nd = nd + 1

print("{} elementos inseridos".format(nd))

#print("##### Ordem #####")
#print(node.inorderPrint(raiz))
#print("##### Pré-ordem #####")
#print(node.preorderPrint(raiz))
#print("##### Pós-ordem #####")
#print(node.postorderPrint(raiz))

#variaveis auxiliares para buscas
arrbusca = arranjo1k
ultimo = ult1k

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
node.buscatree(raiz, 0)
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
node.buscatree(raiz, ultimo)
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
node.buscatree(raiz, -1)
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
    node.buscatree(raiz, num)
    #mede tempo final
    t1 = time.time_ns()
    #calculo do tempo decorrido
    print("Tempo: ", t1 - t0)
    ctrl = ctrl+1

