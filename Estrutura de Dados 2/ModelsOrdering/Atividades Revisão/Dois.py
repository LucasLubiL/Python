def order (vetor,num):
    n = len(vetor)
    vetor.append(n-1)
    aux2:int
    for i in range(n):
        if(num < vetor[i]):
            ind = i
            aux = vetor[i]
            for j in range(n,i,-1):
                vetor[j] = vetor[j-1]
            vetor[i] = num
            break
    
    print(vetor)
            
vetor = [1,2,3,4,6,7,8,9,10]
num:int
print("Digite um numero para colocar no vetor")
num = 5

order(vetor,num)