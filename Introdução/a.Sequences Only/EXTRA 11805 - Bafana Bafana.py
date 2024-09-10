x=int(input())

cont:int
pri:int

pri=0

for i in range(0,x):

    N,K,P= map(int, input().split())

    cont=0

    while cont!=P:
        K=K+1
        if K==N+1:
            K=1
        cont=cont+1
    pri=pri+1
    print(f"Case {pri}: {K}")