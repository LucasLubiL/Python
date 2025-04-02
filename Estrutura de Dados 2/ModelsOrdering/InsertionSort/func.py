def order (vetor, tam):
    aux = 0
    for i in range(10):
        aux = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j]>aux:
            vetor[j+1] = vetor[j]
            j = j - 1
        vetor[j + 1] = aux
            