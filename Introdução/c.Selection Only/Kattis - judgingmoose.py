x,y=map(int, input().split())

if x==0 and y==0:
    print("Not a moose")
elif x==y:
    print(f"Even {x+y}")
elif x<y:
    print(f"Odd {y*2}")
else:
    print(f"Odd {x * 2}")