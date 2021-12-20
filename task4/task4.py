import sys

file = sys.argv[1]
with open(file) as f:
    n = [int(x.rstrip()) for x in f.readlines()]
    f.close()
sred = round(sum(n) / len(n))

print(sum([abs(x - sred) for x in n]))
