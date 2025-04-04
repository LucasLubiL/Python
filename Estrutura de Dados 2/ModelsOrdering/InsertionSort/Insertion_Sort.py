from func import order
import time

inicio = time.time()

vetor = [2,1,5,3,4]
tam = [0]

print("Numeros NÃO ordenados:", end=" ")
print(" ".join(map(str, vetor)))

order(vetor, tam)

print("Numeros ordenados:", end=" ")
print(" ".join(map(str, vetor)))

fim = time.time()

print("Quantiadade passadas: ", tam[0])
print(F"Tempo de execução do programa: {fim - inicio: .8f}")
