def quicksort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivot_index = partition(array, left, right)
        #print(pivot_index)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

def partition(array, left, right):
    j = right
    for i in range ( right - 1 , left - 1 , -1) :
        if array [ i ] > array [ right ]:
            #print("vetor:", array[j])
            array [ i ] , array [ right ] = array [ right ] , array [ i ]
            #j = i
    return j

array = [10,9,8,7,6,5,4,3,2,1]
print("Antes:", array)
quicksort(array)
print("Depois:", array)

# Ao aplicar essa lógica, não se tem ordenação, pois o útlimo é sempre o maior numero e o primeiro sempre o número anterior do maior
# e assim sucessivamente. O grande problema desta abordagem é que toda vez que o array[i] > array[right] o j é recebido com o valor de i da troca
# ou seja, fazendo isso até que o 'for' termine, ocasionando erro grave no retorno do valor, sempre mudando o valor do pivô,
# deixando de ter um pivô correto, e sempre colocando os valores a direita quando encontra um valor menor queo array[i] podendo ter brechas para que
# a ordenação fique comprometida, ao comentar apenas o #j=i o código funciona normal.