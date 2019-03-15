a = [i for i in range(3)]
b = [[j for j in range(3)] for i in range(3)]
b[0][0] = 7
print(b)