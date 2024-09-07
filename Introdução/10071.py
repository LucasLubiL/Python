import sys

for linha in sys.stdin:
   x,y = map(int,linha.split())
   print(x*y*2)