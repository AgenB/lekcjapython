ile = int(input()) // 2 + 1
wyraz = input()
for i in range(ile):
    print("."*(ile - i) + wyraz[ile - i:ile + i + 1] + "."*(ile - i))