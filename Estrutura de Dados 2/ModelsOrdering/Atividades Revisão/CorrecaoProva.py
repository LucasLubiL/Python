# 1) - a lógica é compreencível , porém com detalhes a sereme ajustados, como a variável booelana 
# "Sim", caso fosse "aux" seria melhor, pois não se sabe se o retorno será True ou False.
# Função com correção:

def verifica(lista):
    n = len(lista)
    aux = False
    for i in range (n - 1):
        if lista[i] <= lista[i+1]:
            aux = True
        else:
            aux = False
            break
    return aux

lista = [1,3,2,4,5]
aux = verifica(lista)
print(lista)
print(aux)
        

########################################################################################################

# 2) - Criei a variável "bol" como booleana recebendo True, o segundo "for" tem-se uma iteração menor, com o tamanho -1-i,
#  evitando assim,comparações desnecessárias, logo, se tiver, uma troca de valores, o "bol" recebe False, indicando que 
# houve troca de valores, caso a primeira passada do segundo "for" ficar False, então está desordenado, se manter 
# True , está ordenado e o sistema fecha.

def bubble_sort(array):
    tamanho = len(array)
    bol = True
    for i in range(tamanho - 1):
        for j in range(tamanho-1-i):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
                bol = False
        if bol:
            return bol
    return bol
        
array = [1,2,3,4,5]
bol = bubble_sort(array)
print(array)
print(bol)

########################################################################################################

# 3)  letra D - 16

########################################################################################################

# 4) a - Se fizer essa alteração, o array na posição 0(array[0]) nunca vai ser verificado.
# b - Se fizer essa alteração, o min_index pega a última posição e o segundo "for" começa com "i+1" ou seja, lixo de memória, o sistema da problema
# c - Nesse caso você não teria uma alteração a lógica, mas cria uma situação desnecessária pois não é preciso trocar um número por ele mesmo,
# mesmo que nesse caso v[min-index] fosse o menor número, um número igual a ele estaria logo após ele na lista

########################################################################################################

# 5) Ambos os 2 casos(melhor ou pior caso) tem por percorrência de O(n)², pois independenemte se estiver ou não estiver ordenado, o selection sort
# precisa precorrer os 2 "for" para pegar o menor elemento e comparar se tem outro menor, sendo assim, O(n)², o que muda é quando a lista está quase
# ordenada, sendo feita as mesmas comparações porém com menores trocar possíveis, como array = [1,2,3,5,4] tendo menoas trocas do que um array = [5,4,3,2,1].

########################################################################################################

# 6) O v[i] = x, é totalmente desnecessário , pois ocupa mais espaço de memória, já que se colocar depois de finazliar o while como v[i+1]=aux já
# garante a posição correta. Outro problema é o primeiro "for" começar com (1,n), ou seja, ignorando a primeira posição que seria o (0,n)

########################################################################################################

# 7)

def order(vetor, i):
    n = len(vetor)
    if i == n:
        return
    aux = vetor[i]
    j = i-1
    while j >= 0 and vetor[j] > aux:
        vetor[j+1] = vetor[j]
        j = j - 1
    vetor[j+1] = aux
    order(vetor, i + 1)

vetor = [5,4,3,2,1]
i = 0
order(vetor, i)
print(vetor)
