def order(vetor, i):

    n = len(vetor)
    
    if i == n - 1:
        return
    
    for j in range(n -1 -i):
        if vetor[j] > vetor[j+1]:
            aux = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = aux

    order(vetor, i+1)

vetor = [21,35,41,2,3,6,7,4,1,9,8]

i = 0

order(vetor,i)

print(vetor)