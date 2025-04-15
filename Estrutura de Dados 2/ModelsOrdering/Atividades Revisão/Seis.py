def order(vetor):

    n = len(vetor)
    p = n // 2
    
    for i in range(p):
        menor = vetor[i]
        maior = vetor[n-i-1]
        x = i
        y = n - i
        for j in range(i, n - i):
            if vetor[j] < menor:
                menor = vetor[j]
                x = j
            if vetor[j] > maior:
                maior = vetor[j]
                y = j
        
        aux = vetor[i]
        aux2 = vetor[n - i - 1]
        vetor[i] = menor
        vetor[n - i - 1] = maior
        vetor[x] = aux
        vetor[y] = aux2

vetor = [10,9,8,7,6,5,4,3,2,1]

order(vetor)

print(vetor)