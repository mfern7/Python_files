

ingresenum = int(input("ingrese numero: "))

def collatz(numero):
    if numero % 2 == 0:
        return str(numero) + " // 2 = " + str(numero // 2)
        
    elif numero % 2 == 1:
        return str(numero) + " * 3 + 1 = " + str(3 * numero + 1)

#while collatz(ingresenum) != 1:
print(collatz(ingresenum))
