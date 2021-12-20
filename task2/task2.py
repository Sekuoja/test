import sys

file = sys.argv[1]
with open(file) as f:
    x,y = [float(x) for x in f.readline().split()]
    r = float(f.readline())
    f.close()
file = sys.argv[2]
with open(file) as f:
    points = [(x.split()) for x in f.readlines()]
    f.close()
for a,b in points:
    s = ((x - float(a))**2 + (y - float(b))**2)**0.5
    if s == r:
        print(0)
    elif s < r:
        print(1)
    else:
        print(2)
