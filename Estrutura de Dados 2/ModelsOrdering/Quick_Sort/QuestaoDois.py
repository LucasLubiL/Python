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
array = [random.randint(1, 999) for _ in range(999)]
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
array2 =  [random.randint(1, 999) for _ in range(999)]
quicksort2(array2)
print(array2)
fim2 = time.time()
print(F"Tempo recursivo: {fim2 - inicio2}")