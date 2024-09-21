a = int(input())

for i in range(a):

    x = input().strip()

    if x == "P=NP":
        print("skipped")
    else:
        um,do=map(int,x.split("+"))

        print(um+do)