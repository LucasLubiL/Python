def order (vetor, tam):
    for i in range(10-1):
        for j in range(10-1-i):
            tam[0] += 1
            if vetor[j] > vetor[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
