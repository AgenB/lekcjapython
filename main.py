def nwd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

def nwdMul(a, b, *c):
    d = nwd(a, b)
    for i in c:
        d = nwd(d, i)
    return d

print(nwdMul(12, 18, 33, 60))
