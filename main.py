from random import randrange

def kostka():
    return randrange(1, 7)

x = int(input())
d = {}
s = 0

for _ in range(x):
    i = kostka() + kostka() + kostka()
    d[i] = d.get(i, 0) + 1
    s += i

print("Suma oczek:", s)
print("Statystyki:")

for s in sorted(d):
    print("{} wypadło {:.3%} razy".format(s, d[s] / x))