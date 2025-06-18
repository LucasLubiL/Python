def partition(vetor, left, right):
    pivo = vetor[right]
    i = left - 1

    for j in range(left, right):
        if vetor[j] < pivo:
            i+=1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    
    vetor[i+1], vetor[right] = vetor[right], vetor[i+1]
    return i+1

def quick_sortR(vetor, left = 0, right = None):
    
    if right is None:
        right = len(vetor) - 1
    if left < right:
        pivo = partition(vetor, left, right)
        quick_sortR(vetor, left, pivo - 1)
        quick_sortR(vetor, pivo + 1, right)

def quick_sortI(vetor, left=0, right = None):

    stack = []
    left = 0
    right = len(vetor)-1

    stack.append((left, right))

    while stack:

        left, right = stack.pop()

        if left<right:
            pivo = partition(vetor, left, right)
            stack.append((left, pivo -1))
            stack.append((pivo+1,right))

vetor = [5,4,3,2,1,7,8,9,34,56,12,6,7,23]
vetor2 = [5,4,3,2,1,55,66,77,88,99,1000]

quick_sortR(vetor)
quick_sortI(vetor2)

print(vetor)
print(vetor2)