def quicksort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1  
    print(left, right)
    if left < right:
        pivot_index = partition(array, left, right)  
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)
        
def partition(array, left, right):
    pivot = array[right]
    i = left - 1

    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

array = [77,55,33,99]
print("Antes:", array)
quicksort(array)
print("Depois:", array)

array = [55,44,22,11,66,33]
print("Antes:", array)
quicksort(array)
print("Depois:", array)