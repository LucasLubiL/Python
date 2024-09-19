import sys

x,y=map(int,input().split())

if x==0 and y==1:
    print("ALL GOOD")
    sys.exit(0)
elif x!=0 and y==1:
    print("IMPOSSIBLE")
    sys.exit(0)

b=x/(1-y)

if b.is_integer():
    print(int(b))
else:
    print(f"{b:.9f}")


