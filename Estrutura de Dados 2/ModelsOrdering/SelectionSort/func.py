def order (vetor, tam):
    for i in range(10):
        menor = vetor[i]
        x = i
        for j in range(i, 10):
            if(vetor[j] < menor):
                menor = vetor[j]
                x = j     
        if(i!=x): 
            aux = vetor[i]
            vetor[i] = menor
            vetor[x] = aux
