import time
import random

def quicksort(array, left=0, right=None):
    j = partition ( array , left , right )
    if ( left < j - 1) :
        quicksort ( array , left , j - 1)
    if ( j + 1 < right ) :
        quicksort ( array , j + 1 , right )

def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

inicio = time.time()
array = [random.randint(1, 100) for _ in range(10)]
left = 0
right= len(array) - 1
print("Antes:",array)
quicksort(array, left, right)
print("Depois:",array)
fim = time.time()
print(F"Tempo de execução: {fim - inicio}")

# Se você implementar esse código, tem que declarar o left e o right antes mesmo da primeira chamada da
# função quicksort(), pois nessa nova implementação, dentro da fun ção o right não é declarado com o tamnaho do array
# fazendo ele ser None já que no parâmetro da função o right tem que receber o None, caso não fizer, o código é quebrado e não roda.
# Fazendo-se essas mudanças, não houve falhas na ordenação, ainda sim teve-se a ordenação correta e com tempo de execução
# aceitável e funcional. 