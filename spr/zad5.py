text = "AbraKaDabra Brak kadr"

litery = 0
wyrazy = 0
for i in text:
    if(i != " "): litery += 1
text2 = text.split()
wyrazy = len(text2)
print("wyrazów:" + str(wyrazy) + ", liter:" + str(litery))
 
