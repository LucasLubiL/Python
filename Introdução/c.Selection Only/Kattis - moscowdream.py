a,b,c,d=map(int, input().split())

if a>=1 and b>=1 and c>=1 and d>=3:
    if a+b+c>=d:
       print("YES")
    else:
       print("NO")
else:
    print("NO")