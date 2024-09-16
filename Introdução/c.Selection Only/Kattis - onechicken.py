x,y=map(int, input().split())

if y>=x:
    if y-x==1:
        print(f"Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print(f"Dr. Chaz will have {y-x} pieces of chicken left over!")
else:
    if x-y==1:
        print(f"Dr. Chaz needs 1 more piece of chicken!")
    else:
        print(f"Dr. Chaz needs {x-y} more pieces of chicken!")