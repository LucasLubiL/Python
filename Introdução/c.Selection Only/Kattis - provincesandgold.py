x,y,z=map(int,input().split())

um=int(x*3)
dois=int(y*2)
tres=int(z*1)

soma=int(um+dois+tres)

if soma<=1:
    print("Copper")
elif soma==2:
    print("Estate or Copper")
elif soma>2 and soma<5:
    print("Estate or Silver")
elif soma==5:
    print("Duchy or Silver")
elif soma>=6 and soma<8:
    print("Duchy or Gold")
elif soma>=8:
    print("Province or Gold")

