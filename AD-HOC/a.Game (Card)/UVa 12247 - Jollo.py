while True:

    a,b,c,x,y=map(int, input().split())
    if a==0 and b==0 and c==0 and x==0 and y==0:
        break

    princesa = sorted([a,b,c])
    maiorPrincesa=princesa[2]
    medioPrincesa=princesa[1]
    menorPrincesa=princesa[0]

    principe = sorted([x,y])
    maiorPrincipe=principe[1]
    medioPrincipe=principe[0]
    menor:int

    if maiorPrincipe > maiorPrincesa:
        z=0
        if medioPrincipe > maiorPrincesa:
            for i in range(1,53):
                if i!=a and i!=b and i!=c and i!=x and i!=y:
                    print(i)
                    z=1
                    break
            if z==0:
                print("-1")
        elif medioPrincipe > medioPrincesa:
            for i in range(1,53):
                if i!=a and i!=b and i!=c and i!=x and i!=y and i>medioPrincesa:
                    print(i)
                    z=1
                    break
            if z==0:
                print("-1")
        elif medioPrincipe > menorPrincesa:
            for i in range(1,53):
                if i!=a and i!=b and i!=c and i!=x and i!=y and i>maiorPrincesa:
                    print(i)
                    z=1
                    break
            if z == 0:
                print("-1")
        else:
            z=0
            for i in range(1, 53):
                if i != a and i != b and i != c and i != x and i != y and i > maiorPrincesa:
                    print(i)
                    z=1
                    break
            if z==0:
               print("-1")
    else:
        if maiorPrincipe > medioPrincesa:
            z=0
            if medioPrincipe > medioPrincesa:
                for i in range(1, 53):
                    if i != a and i != b and i != c and i != x and i != y and i > medioPrincesa:
                        print(i)
                        z=1
                        break
                if z==0:
                    print("-1")
            else:
                 print("-1")
        else:
            print("-1")






