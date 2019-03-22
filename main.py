d = {}
for _ in range(int(input())):
    for i in input(): d[i] = d.get(i, 0) + 1
a = list(d.items()
a.sort(key=lambda x: x[0].swapcase())
for i in a[1:]: print(i[0], i[1])