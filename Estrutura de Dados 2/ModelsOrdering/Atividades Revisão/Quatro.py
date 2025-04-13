def order(vetor, i):
    
    n = len(vetor)
    
    if i == n:
        return
       
    menor = vetor[i]
    x= i

    for k in range (i, n):
        if vetor[k] < menor:
            menor = vetor[k]
            x = k
        
    if i!=x:
        aux = vetor[i]
        vetor[i] = menor
        vetor[x] = aux
        
    order(vetor, i + 1)
    
vetor = [5,4,3,2,1]

i = 0

order(vetor, i)

print(vetor)