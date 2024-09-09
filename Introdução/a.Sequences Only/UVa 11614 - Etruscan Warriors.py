x=int(input())

aux:int
fila:int
cont:int

for i in range(0,x):

   fila=0
   cont=0
   aux=1

   y=int(input())

   for j in range(0,y):
       if j==0:
           fila=fila+1
       elif aux==cont:
           aux=aux+1
           fila=fila+1
           cont=0
       else :
           cont=cont+1

   print(fila)