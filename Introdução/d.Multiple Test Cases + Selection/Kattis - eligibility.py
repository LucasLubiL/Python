va=int(input())

for i in range(a):

    x=input()

    parte = x.split()

    data1=list(map(int, parte[1].split('/')))
    data2=list(map(int, parte[2].split('/')))

    d1=data1[0]
    d2=data2[0]
    sem=int(parte[3])

    if d1>=2010 or d2>=1991:
        print(f"{parte[0]} eligible")
    elif sem>40:
        print(f"{parte[0]} ineligible")
    else:
        print(f"{parte[0]} coach petitions")