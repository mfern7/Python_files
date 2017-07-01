name = ''                           # (1)
intentos = 0
while name != 'MARCOS' and intentos < 3:          # (2)
    print('Please type your name.')
    name = input()                  # (3)
    intentos = intentos + 1
print('Thank you!')     
