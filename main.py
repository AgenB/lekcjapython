a = [1, 3, 6, 8]
b = list(map((lambda x, y: x**y), a, a))
print(b)
