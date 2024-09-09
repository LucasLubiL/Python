import sys

for i in sys.stdin:
    x,y= map(int, i.split())
    print(x*y*2)
