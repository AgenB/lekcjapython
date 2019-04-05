text = "AbraKaDabra Brak kadr"

d = {}
for i in text.upper():
    if(i != " "):
        d[i] = d.get(i, 0) + 1
for i in d.items():
    print(str(i[0]) + ":" + str(i[1]), end = " ")
print()
