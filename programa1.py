# This program says hello and asks for my name.

intentos = 0

name1 = input("ingrese su nombre: ")
#print("ingrese su nombre: " + name1)
if name1 == 'Mary':
    print('Hello Mary')
elif name1 == "Jorge":
    print(name1 * 3)
else:
    print("ususario incorrecto")
    
    while intentos > 3:          # (2)
        name1 = input("ingrese de nuevo su nombre: ")
        #print('Please type your name.')
        #name = input() 
        intentos = intentos + 1
              
password = input("ingrese su pass: ")
#print("ingrese su pass: " + password)
if password == '123456':
   print('Access granted.')
else:
   print('Wrong password.')

print('Hello world!')
print('What is your name?')    # ask for their name
print()
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
