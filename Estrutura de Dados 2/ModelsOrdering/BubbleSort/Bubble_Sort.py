from func import order

print("Digite 10 numeros para poder ordenar: ")

vetor = []
tam = [0]

# Neste for se faz a leitura do inteiro para se colocar no vetor;
for i in range(10):
    x = int(input())
    vetor.append(x)

# vetor nao ordenado;
print("Numeros NÃO ordenados:", end=" ")
print(" ".join(map(str, vetor)))

# Aqui chama-se uma função com os 2 parametros, vetor e um contador;
order(vetor, tam)

# Já o vetor em ordem crescente;
print("Numeros ordenados:", end=" ")
print(" ".join(map(str, vetor)))

# Quantas vezes houve a iteração.
print("Quantiadade passadas: ", tam[0])
