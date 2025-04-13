def order (vetor, i):
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

    order(vetor, i + 1)

vetor = [3,7,4,6,1,9,2,11,45,34,90,67,66]

i = 0

order(vetor, i)

print(vetor)