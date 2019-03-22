a = {"ala": 15, "janek": 20}
a[4] = 5
a[(2, 3, 4)] = "krotka"
print(a)
print(a.items())
print(a.keys())
print(a.values())
print("ala" in a)
print(a.get("aa", "nie ma"))
print(a.get("ala", "nie ma"))