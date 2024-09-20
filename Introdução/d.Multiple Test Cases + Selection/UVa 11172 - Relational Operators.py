x=int(input())

for i in range(x):
    y,z=map(int, input().split())

    if y<z:
        print("<")
    elif y>z:
        print(">")
    else:
        print("=")