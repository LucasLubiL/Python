import random
import time

def merge(a, b):

    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    while i < len(a):
        c.append(a[i])
        i += 1
    
    while j < len(b):
        c.append(b[j])
        j += 1

    return c

def merge_sortI(arr):

    step = 1
    length = len(arr)

    while step < length:

        for i in range(0, length, 2 * step):
        
            left = arr[i:i + step]
            right = arr[i + step:i + 2 * step]

            merged = merge(left, right)
    
    
            for j, val in enumerate(merged):
                arr[i + j] = val

        step *= 2

    return arr

def merge_sortR(array):

    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    esq = array[:mid]
    dir = array[mid:]

    sorEsq = merge_sortR(esq)
    sorDir = merge_sortR(dir)

    return merge(sorEsq, sorDir)

inicio = time.time()
array = random.sample(range(1, 101), 5)
ord = merge_sortI(array)
print("Array: ",ord)
fim = time.time()
print(F"Time: {fim - inicio:.6f}")


inicio2 = time.time()
array2 = random.sample(range(1,101), 5)
ord = merge_sortR(array2)
print("Array 2: ", ord)
fim2 = time.time()
print(F"Time: {fim2 - inicio2:.6f}")

# O tempo de execução do recursivo foi mais rápido em tempo de execuçao do que a versão interativa,
# ou seja, com uma grande vantagem em cima da versão interativa, a grande vantagem da recursiva é que
# ela faz a ordenação de forma "direta", sem a necessidade de fazer as verificações e chamadas de função 
# que leva tempo e espaço de memória, enquanto a versão interativa tem-se mais um tempo de execução e mais 
# passadas para poder alocar os valores na posição correta, apesar de também ser bem eficaz, já a versão recursiva
# tendo tempo de execução menor pois faz a divisão do array até o menor número possível para que já seja formatada
# em ordem crescente ou decrescente de forma direta sem enrolações.
