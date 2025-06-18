def merge(a, b):

    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1

    while i<len(a):
        c.append(a[i])
        i+=1

    while j<len(b):
        c.append(b[j])
        j+=1

    return c

def merge_sortI(vetor):

    step = 1
    leng = len(vetor)

    while step < leng:
       
        for i in range(0,leng, 2*step):
           
            esq = vetor[i:i+step]
            dir = vetor[i+step:i+2*step]

            merged = merge(esq,dir)

            for j, val in enumerate(merged):
                vetor[i+j] = val
            
        step*=2  
   
    return vetor


def merge_sortR(vetor):

    if  len(vetor)<=1:
        return vetor
    
    mid = len(vetor)//2
    esq = vetor[:mid]
    dir = vetor[mid:]

    mEsq = merge_sortR(esq)
    mDir = merge_sortR(dir)

    return merge(mEsq,mDir)

vetor = [5,4,3,2,5,4,3,2,1,1,1,1]

ord = merge_sortI(vetor)
ord2 = merge_sortR(vetor)

print(ord)
print(ord2)