from func import order

print("Digite 10 numeros para poder ordenar: ")

vetor = []
tam = [0]

for i in range(10):
    x = int(input())
    vetor.append(x)

order(vetor, tam)

print("Numeros ordenados")
for i in range(10):
    print(vetor[i])

print("Quantiadade passadas: ", tam[0])
