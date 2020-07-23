#! python3

def f():
    i = input("Podaj liczbe: ")

    try:
        if int(i) <= 6:
            print("super")
        else:
            print("nie fajno")
    except:
        print("Sprobuj jeszcze raz i podaj liczbe!")
        f()
f()
