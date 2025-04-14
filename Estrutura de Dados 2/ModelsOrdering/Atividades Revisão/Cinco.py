def order(vetor):
    
    n = len(vetor)

    for i in range(n-1):
        maior = vetor[i]
        x = i
        for j in range(i,n):
            if vetor[j] > maior:
                maior = vetor[j]
                x = j
        if i!=x:
            aux = vetor[i]
            vetor[i] = maior
            vetor[x] = aux

vetor = [1,2,3,4,5,6,7,8,9,10]

order(vetor)
print(vetor)