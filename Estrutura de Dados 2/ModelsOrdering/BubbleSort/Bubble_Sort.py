from func import order

print("Digite 10 numeros para poder ordenar: ")

vetor = []

for i in range(10):
    x = int(input())
    vetor.append(x)

order(vetor)

print("Numeros ordenados")
for i in range(10):
    print(vetor[i])