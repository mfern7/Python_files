catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    if name in catNames:
        print('el valor ya existe')
        continue
    else:
        print('no hay gatos con nombre ' + name)
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for nam in catNames:
    print('  ' + nam)
if 'gato3' not in catNames:
    print('---> gato3 no esta en la lista')
else:
    print('lista completa')


dogsNames = []
while True:
    print('Enter the name of dogs ' + str(len(dogsNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    dogsNames = dogsNames + [name] # list concatenation
print('The dogs names are:')
for nam in dogsNames:
    print('  ' + nam)
    
print('Estas son todas las mascotas:')
pets = catNames + dogsNames
for name in pets:
    print("           " + name)

print(str(catNames + dogsNames), end='\n')

print("-" * 30)

for i in range(len(pets)):
    print('Index ' + str(i) + ' in supplies is: ' + pets[i])
