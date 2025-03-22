def order (vetor, tam):
    for i in range(10):
        menor = vetor[i]
        x = i
        for j in range(i, 10):
            if(vetor[j] < menor):
                menor = vetor[j]
                x = j     
        if(i!=x): 
            tam[0] += 1
            aux = vetor[i]
            vetor[i] = menor
            vetor[x] = aux
            print("--------------------------------------------")
            print(F"Iteração {i+1}: ")
            print(F"Troca realizada: {vetor[i]} com {vetor[x]}")
            print(" " .join(map(str, vetor)))