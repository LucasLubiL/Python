def merge(a, b):

    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
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

def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid = len(array)//2
    esq = array[:mid]
    dir = array[mid:]

    sorEsq = merge_sort(esq)
    sorDir = merge_sort(dir)

    return merge(sorEsq, sorDir)

array = [5,4,3,2,1]

ord = merge_sort(array)

print(ord)