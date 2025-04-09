def order (vetor):
    n = len(vetor)
    for i in range(1,n-1):
        if vetor[i]<vetor[i-1]:
            return print("NAO ORDENADO")
    print("ORDENADO")

print("Digite 10 numeros para poder ordenar: ")

vetor = []

for i in range(10):
    x = int(input())
    vetor.append(x)

order(vetor)
