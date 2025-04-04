def order (vetor, tam):
    aux = 0
    n = len(vetor)
    for i in range(n):
        aux = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j]>aux:
            vetor[j+1] = vetor[j]
            j = j - 1
            tam[0] = tam[0] + 1
        vetor[j + 1] = aux
