ile = 0
while True:
    try:
        x = int(input())
        ile += 1
    except KeyboardInterrupt as e:
        print()
        break
    except:
        pass
print(ile)