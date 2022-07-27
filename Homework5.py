#Написати 5 прикладів циклу while.
while True:
  print("Type Ctrl-C to stop me!")
# while 2
x = 'polish'
while x:
    print(x,end='')
x = x[2:]
# while 3
a = 13
b = 10
while a < b:
    print(a, end='')
a += 1
# while 4
i = 1
while i < 6:
   print(i)
  if i == 3:
    break
    i += 1
# while 5
i = 5
while i <= 10:
   print(i ** 2)
    i += 1
#Написати 5 прикладів while : else конструкції
#1 проходишься по корзине: если такой фрукт есть - тебе выведется количество, а если нет, то можно будет его добавить
basket = [
    {'fruit': 'apple', 'qty': 20},
    {'fruit': 'banana', 'qty': 30},
    {'fruit': 'orange', 'qty': 10}
]

fruit = input('Enter a fruit:')

index = 0
found_it = False

while index < len(basket):
    item = basket[index]
    # check the fruit name
    if item['fruit'] == fruit:
        found_it = True
        print(f"The basket has {item['qty']} {item['fruit']}(s)")
        break

    index += 1

if not found_it:
    qty = int(input(f'Enter the qty for {fruit}:'))
    basket.append({'fruit': fruit, 'qty': qty})
    print(basket)
    
 #2 проходишься по лакам и проверяешь есть/нет того или иного цвета
nailpolish = [
    {'color': 'red', 'qty': 20},
    {'color': 'blue', 'qty': 12},
    {'color': 'black', 'qty': 13}
]
color = input('Enter a color:')

index = 0
found_it = False

while index < len(nailpolish): #len Return the length (the number of items) of an object. The argument may be a sequence (string, tuple or list) or a mapping (dictionary).
    item = nailpolish[index]
    # check the nailpolish color
    if item['color'] == color:  # проверка строки 8
        found_it = True
        print(f"You have {item['qty']} bottles of {item['color']} nailpolish")
        break
    index += 1

if not found_it:
    qty = int(input(f'Enter the qty for {color}:'))
    nailpolish.append({'color': color, 'qty': qty})
    print(nailpolish)

#3 while: если число больше 22 - выходим из цикла 
data = 3
while data < 22:
    print(data)
    data += 1
else:
    print("data is no longer less than 22")    
    
#4 while: если число больше 22 - выходим из цикла 
data = 3
while data < 22:
    print(data)
    data += 1
else:
    print("data is no longer less than 22") 


#5 while: если число больше 22 - выходим из цикла 
data = 3
while data < 22:
    print(data)
    data += 1
else:
    print("data is no longer less than 22") 

#Написати 3 приклади з break у середині.
#1 выходим из цикла если в слове оказывается буква "e" или "b"
animal = "dog"
i = 0
while True:
    print(animal[i])
    if animal[i] == "e" or animal[i] == "b":
        break
    i += 1
print("Out of doge loop")

#2 ищем есть ли четное количество в нашем списке количества ошибок учеников

errors = [3, 7, 6, 7, 3, 9, 3]
numErr = False
i = 0
while i < len(errors):
    print(i)
    numErr = errors[i] % 2 == 0
    if numErr:
        break
    i += 1 #!!!!!

print(numErr)

#3 



#Написати 3 приклади з continue у середини.


   
    
    
    
    
   
    
