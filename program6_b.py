#ingresenum = None

while True:
    
    try:
        global ingresenum
        ingresenum = int(input("ingrese numero: "))
        break
    except ValueError:
        print("Error: Ingrese solo numero ")
    

while ingresenum != 1:
   if ingresenum % 2 == 0:
      par = ingresenum // 2
      print(str(ingresenum) + " // 2 = " + str(par))
      ingresenum = par
        
   elif ingresenum % 2 == 1:
      impar = 3 * ingresenum + 1
      print(str(ingresenum) + " * 3 + 1 = " + str(impar))
      ingresenum = impar
