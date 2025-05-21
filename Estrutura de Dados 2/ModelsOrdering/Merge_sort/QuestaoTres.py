def merge(a, b):

    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    
    while i < len(a):
        c.append(a[i])
        i += 1
    
    while j < len(b):
        c.append(b[j])
        j += 1

    return c

def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid =  (len(array) - 1)// 2
    esq = array[:mid]
    dir = array[mid:]

    sorEsq = merge_sort(esq)
    sorDir = merge_sort(dir)

    return merge(sorEsq, sorDir)

array = [1,2,3,4,5,6,3,2,9,6,4,0,3]

print(array)

ord = merge_sort(array)

print(ord)

# a) No +1 não houve diferenças, o resultado foi o mesmo
# b) Funcionou apenas para o +1
# c) No -1 houve falha do sistema, pois irá descarta um valor importante do array para dividir para esquerda e para a direita, que acaba pegando lixo de memória