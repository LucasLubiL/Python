x=int(input())
um:float
do:float
tres:float
mod:float

for i in range(x):
    y=int(input())

    um=(y*567)/9
    do=(um+7492)*235
    tres=(do/47)-498

    tres=abs(tres)

    mod=int(tres%100)//10

    print(mod)