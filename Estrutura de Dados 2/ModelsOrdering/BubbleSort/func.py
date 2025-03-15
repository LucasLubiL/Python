# Aqui faz toda a verificação do vetor, analisando se um numero é maior que o numero da proxima posição;

def order (vetor, tam):
    for i in range(10-1):
        for j in range(10-1-i):
            # Este 'tam' é acrescentado cada vez que se tem uma interção com o for, para se saber quantas vezes ele foi executado (FORMA OTIMIZADA).
            tam[0] += 1
            if vetor[j] > vetor[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
