def nwd(a, b):
    while (b != 0):
        a, b = b, a % b
    return a

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(nwd(a, b))