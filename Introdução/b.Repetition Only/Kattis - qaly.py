x=int(input())
soma:float
soma=0

for i in range(x):
    y,z=map(float, input().split())
    soma=soma+(y*z)

print(f"{soma:.3f}")