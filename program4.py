
def spam(dividir):
    try:
        return 42 / dividir
    except ZeroDivisionError:
        print("Error en el numero elegido")
    except TypeError:
        print("Error cualquiera")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
print(spam("egg"))


    
