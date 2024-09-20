x=input()
cont:int

cont=1

while x!="#":

    if x=="HELLO":
        print(f"Case {cont}: ENGLISH")
        cont=cont+1
    elif x=="HOLA":
        print(f"Case {cont}: SPANISH")
        cont=cont+1
    elif x=="HALLO":
        print(f"Case {cont}: GERMAN")
        cont=cont+1
    elif x=="BONJOUR":
        print(f"Case {cont}: FRENCH")
        cont=cont+1
    elif x=="CIAO":
        print(f"Case {cont}: ITALIAN")
        cont=cont+1
    elif x=="ZDRAVSTVUJTE":
        print(f"Case {cont}: RUSSIAN")
        cont=cont+1
    else:
        print(f"Case {cont}: UNKNOWN")
        cont=cont+1

    x = input()
