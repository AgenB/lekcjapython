try:
    x = int(input())
    print(1 / x)
except ZeroDivisionError:
    print("Nie wolno dzielić przez 0")
except ValueError:
    print("Miałeś podać liczbę całkowitą 😣 ")
except Exception as e:
    print("Coś poszło nie tak 😣 ", type(e))