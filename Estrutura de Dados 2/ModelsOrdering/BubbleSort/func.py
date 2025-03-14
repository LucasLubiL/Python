def order (vetor):
    for i in range(10-1):
        for j in range(10-1-i):
            if vetor[j] > vetor[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
