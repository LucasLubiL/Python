import random

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

def merge_sort(arr):

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

array = [1,2,3,4,5]
array2 = [1,2,3,4,5,6,7,8,9,10]
array3 = random.sample(range(1, 101), 20)

print("Arrays normais:")
print("Array 1:", array)
print("Array 2:", array2)
print("Array 3:", array3)

print("--------------------------------")

ord = merge_sort(array)
print("Array 1: ",ord)

ord = merge_sort(array2)
print("Array 2: ",ord)

ord = merge_sort(array3)
print("Array 3: ",ord)