# Lucas Amaral Luciano

# Quesão 1

def order (vetor):
    n = len(vetor)
    for i in range(1,n-1):
        if vetor[i]<vetor[i-1]:
            return print("NAO ORDENADO")
    print("ORDENADO")

print("Digite 10 numeros para poder ordenar: ")

vetor = []

for i in range(10):
    x = int(input())
    vetor.append(x)

order(vetor)


###############################################################
#Questão 2

def order2 (vetor,num):
    n = len(vetor)
    vetor.append(n-1)
    aux2:int
    for i in range(n):
        if(num < vetor[i]):
            ind = i
            aux = vetor[i]
            for j in range(n,i,-1):
                vetor[j] = vetor[j-1]
            vetor[i] = num
            break
    
    print(vetor)
            
vetor2 = [1,2,3,4,6,7,8,9,10]
num:int
num = 5

order2(vetor2,num)

###############################################################
#Questão 3

def order3 (vetor, i):
    aux:int
    n = len(vetor)

    if i == n:
        return
    
    aux = vetor[i]
    j = i - 1

    while j>=0 and vetor[j] > aux:
        vetor[j+1] = vetor[j]
        j = j - 1
    vetor[j+1] = aux

    order3(vetor, i + 1)

vetor3 = [3,7,4,6,1,9,2,11,45,34,90,67,66]

i = 0

order3(vetor3, i)

print(vetor3)

###############################################################
#Questão 4

def order4(vetor, i):
    
    n = len(vetor)
    
    if i == n:
        return
       
    menor = vetor[i]
    x= i

    for k in range (i, n):
        if vetor[k] < menor:
            menor = vetor[k]
            x = k
        
    if i!=x:
        aux = vetor[i]
        vetor[i] = menor
        vetor[x] = aux
        
    order4(vetor, i + 1)
    
vetor4 = [5,4,3,2,1]

i = 0

order4(vetor4, i)

print(vetor4)

###############################################################
#Questão 5

def order5(vetor):
    
    n = len(vetor)

    for i in range(n-1):
        maior = vetor[i]
        x = i
        for j in range(i,n):
            if vetor[j] > maior:
                maior = vetor[j]
                x = j
        if i!=x:
            aux = vetor[i]
            vetor[i] = maior
            vetor[x] = aux

vetor5 = [1,2,3,4,5,6,7,8,9,10]

order5(vetor5)
print(vetor5)

###############################################################
#Questão 6

def order6(vetor):

    n = len(vetor)
    p = n // 2
    
    for i in range(p):
        menor = vetor[i]
        maior = vetor[n-i-1]
        x = i
        y = n - i
        for j in range(i, n - i):
            if vetor[j] < menor:
                menor = vetor[j]
                x = j
            if vetor[j] > maior:
                maior = vetor[j]
                y = j
        
        aux = vetor[i]
        aux2 = vetor[n - i - 1]
        vetor[i] = menor
        vetor[n - i - 1] = maior
        vetor[x] = aux
        vetor[y] = aux2

vetor6 = [10,9,8,7,6,5,4,3,2,1]

order6(vetor6)

print(vetor6)