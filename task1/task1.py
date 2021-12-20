import sys

file = sys.argv[1]
with open(file) as f:
    m = int(f.readline())
    n = int(f.readline())
    f.close()

a = "".join([str(x) for x in range(1, m+1)])

step = n-1
rez = "1"
while True:
    if a[step % m] not in rez:
        rez += a[step % m]
    else:
        break
    step += n-1
print(rez)
