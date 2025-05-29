import time
import random

def quicksort(array, left=0, right=None):
    stack = []
    left, right = 0, len(array) - 1
    
    stack.append((left, right))
    
    while stack:
        left, right = stack.pop()
        
        if left < right:
            pivot_index = partition(array, left, right)
            
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))

def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

inicio = time.time()
array = [random.randint(1, 101) for _ in range(100)]
quicksort(array)
print(array)
fim = time.time()
print(F"Tempo Iterativo: {fim - inicio}")

def quicksort2(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

inicio2 = time.time()
array2 =  [random.randint(1, 101) for _ in range(100)]
quicksort2(array2)
print(array2)
fim2 = time.time()
print(F"Tempo recursivo: {fim2 - inicio2}")

# Ao comparar os 2 codigos, iterativo e recursivo, pode-se perceber que a versão iterativa na maioria das vezes
# tende-se a ter um tempo de processamento menor do que a recursiva, um pouco contraditório, já que a recursiva usa-se 
# "menas" linhas de códigos e com uma clareza melhor no código, porém deve-se relatar que o quick sort tende-se a ser 
# uma lógica de ordenação bem melhor com grandes vetores, fiz o teste com vetores menores, médios e grandes.
# Em vetores menores, o recursivo teve um melhor desempenho, já que se usou menos espaços de memória, enquanto com 
# vetores médios, teve-se um tempo de execução aproximados, relativamente próximos, enquanto com vetores maiores, a versão
# iterativa teve um melhor desempenho com melhor tempo de execução mais do que a recursiva, já que ela foi apropriadamente deita
# para o quick sort , sendo assim 'n log n', por isso que a recursiva se saiu bem em vetores bem menores, pois o quick sort
# foi e é feito para grandes vetores