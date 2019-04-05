text = "AbraKaDabra Brak kadr"

t = text.split()
x = []
for i in t:
	x.append(i[::-1])
text2 = " ".join(x)
print(text2)
