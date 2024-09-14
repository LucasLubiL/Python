m=int(input())
n=int(input())
cont:int
soma:int
soma=0

for i in range(n):
    num=int(input())
    cont=m-num
    soma=soma+cont

print(soma+m)