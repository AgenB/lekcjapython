d = {}
s = input()
m = s[0]
for i in s:
    d[i] = d.get(i, 0) + 1
    if(d[i] > d[m]):
        m = i
print(d)
print(m + ", " + str(d[m]))
print("\n")
a = list(d.items())
a.sort(key = lambda k: k[1], reverse = True)
print(a)
print(a[0])