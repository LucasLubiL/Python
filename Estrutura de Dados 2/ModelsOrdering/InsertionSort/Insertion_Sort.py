from func import order

print("Digite 10 numeros para poder ordenar: ")

vetor = []
tam = [0]

for i in range(10):
    x = int(input())
    vetor.append(x)

print("Numeros NÃO ordenados:", end=" ")
print(" ".join(map(str, vetor)))

order(vetor, tam)

print("Numeros ordenados:", end=" ")
print(" ".join(map(str, vetor)))

print("Quantiadade passadas: ", tam[0])