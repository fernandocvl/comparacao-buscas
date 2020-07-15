class newNode: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = self.parent = None

def insert(root, key): 
	newnode = newNode(key) 
	x = root 
	y = None
	while (x != None): 
		y = x 
		if (key < x.key): 
			x = x.left 
		else: 
			x = x.right 
	if (y == None): 
		y = newnode 
	elif (key < y.key): 
		y.left = newnode 
	else: 
		y.right = newnode 
	return y 

def buscatree(root, key): 
        if root is None:
            print("{} Not found!".format(key))
            return
        if root.key == key: 
            print("{} Found!".format(root.key))
            return
        if root.key < key: 
            return buscatree(root.right, key) 
        return buscatree(root.left, key)

def inorderPrint(root): 
	if (root == None): 
		return
	else: 
		inorderPrint(root.left) 
		print(root.key, end = " ")
		inorderPrint(root.right) 

def preorderPrint(root):
        if (root == None):
                return
        else:
                print(root.key, end = " ")
                preorderPrint(root.left)
                preorderPrint(root.right)

def postorderPrint(root):
        if (root == None):
                return
        else:
                postorderPrint(root.left)
                postorderPrint(root.right)
                print(root.key, end = " ")




#incio dos testes
import time
import random
import sys
sys.setrecursionlimit(10**7)

#variaveis auxiliares ult elemento dos arranjos
ultimo = 9999

#popula arvore
raiz = None
valraiz = ultimo//2  #raiz valor inteiro de n/2
raiz = insert(raiz, valraiz)  #insere raiz

#q1
valq1 = ultimo//4  #q1 valor inteiro de n/4
insert(raiz, valq1)  #insere q1

#q3
valq3 = (ultimo//4)*3  #q3 valor inteiro de (n/4)*3
insert(raiz, valq3)  #insere q3

print(valq1)
print(valraiz)
print(valq3)

random.seed(ultimo)
arrq1 = random.sample(range(0, valq1), valq1)
arrq2 = random.sample(range(valq1 +1, valraiz), (valraiz - valq1)-1)
arrq3 = random.sample(range(valraiz +1, valq3), (valq3 - valraiz)-1)
arrq4 = random.sample(range(valq3 +1, ultimo+1), (ultimo - valq3))

ctrl = 0
for i in arrq1:
        insert(raiz, i)
        ctrl = ctrl + 1

for i in arrq2:
        insert(raiz, i)
        ctrl = ctrl + 1

for i in arrq3:
        insert(raiz, i)
        ctrl = ctrl + 1

for i in arrq4:
        insert(raiz, i)
        ctrl = ctrl + 1

print("{} elementos inseridos".format(ctrl+3))
#buscatree(raiz, 2)
#inorderPrint(raiz)

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
buscatree(raiz, valraiz)
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
buscatree(raiz, ultimo)
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
buscatree(raiz, -1)
#mede tempo final
t1 = time.time_ns()
#calculo do tempo decorrido
print("Tempo: ", t1 - t0)
ctrl=ctrl+1

arrbusca = list(range(0, ultimo+1))
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
    buscatree(raiz, num)
    #mede tempo final
    t1 = time.time_ns()
    #calculo do tempo decorrido
    print("Tempo: ", t1 - t0)
    ctrl = ctrl+1

