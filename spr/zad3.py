t = "AbraKaDabra Brak kadr"
y = ""
for i in range(len(t)):
	if(i%2==0):
		x = t[i:i+2]
		y = y + x[::-1]
print(y)
