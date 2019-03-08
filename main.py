def silnia(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

def silniaR(n):
    if (n == 0):
        return 1
    else:
        return n * silniaR(n - 1)

def nwd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

print(nwd(12,18))