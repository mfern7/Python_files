intentos = 0

# while and If
while True and intentos < 3:
  print('Who are you?')
  name = input()
  if name != 'Joe':       #(1)
    intentos = intentos + 1
    continue              #(2)
  print('Hello, Joe. What is the password? (It is a fish.)') 
  password = input()      #(3)
  if password == 'swordfish':
    break                 #(4)
print('Access granted.')  #(5)

# for 
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')
    
total = 0               #(1)
for num in range(101):  #(2)
   total = total + num  #(3)
print(total)            #(4)

def nombre():
    print("Esto es un print...")

nombre()

