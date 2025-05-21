class Node:
    def inicializa(self, valor):
        self.valor = valor
        self.next = None

class Lista:
    def iniciar(self):
        self.first = None
        self.last = None

    def empty(self):
        return self.first is None

    def pushBack(self, valor):
        novo = Node()
        novo.inicializa(valor)
        
        if self.empty():
            self.first = novo
            self.last = novo
        else:
            self.last.next = novo
            self.last = novo

    def imprimir(self):
        atual = self.first
        while atual is not None:
            if atual.next is not None:
                print(atual.valor, end=' ')
            else:
                print(atual.valor)
            atual = atual.next

    def getMiddle(self, head):
        if head is None:
            return head

        lento = head
        rapido = head.next

        while rapido is not None and rapido.next is not None:
            lento = lento.next
            rapido = rapido.next.next

        return lento

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.valor <= b.valor:
            resultado = a
            resultado.next = self.merge(a.next, b)
        else:
            resultado = b
            resultado.next = self.merge(a, b.next)

        return resultado

    def mergeSort(self, head):
        if head is None or head.next is None:
            return head

        meio = self.getMiddle(head)
        direito = meio.next
        meio.next = None

        esquerda_ordenada = self.mergeSort(head)
        direita_ordenada = self.mergeSort(direito)

        return self.merge(esquerda_ordenada, direita_ordenada)

    def ordenar(self):
        self.first = self.mergeSort(self.first)

lista = Lista()
lista.iniciar()

for valor in [5,4,3,2,1]:
    lista.pushBack(valor)

print("Antes de ordenar:")
lista.imprimir()

lista.ordenar()

print("Depois de ordenar:")
lista.imprimir()