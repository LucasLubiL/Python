x=input()
pala:str

parte=x.split()
pala=parte[0]
num=int(parte[1])

if pala=='OCT' and num==31 or pala=='DEC' and num==25:
    print("yup")

else:
    print("nope")