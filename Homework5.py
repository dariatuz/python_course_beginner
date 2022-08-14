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

     
#  аписати 5 прикладів while : else конструкції

#1
data = 3
while data < 22:
    print(data)
    data += 1
else:
    print("data is no longer less than 22")    
    
#2 
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


#3
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)
else:
    print("Loop is finished")

#4
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        continue
    print(n)
else:
    print("Loop is finished")

#5
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print('much better')

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

print('-- Help: type quit to exit --')
while True:
    color = input('Enter your favorite color:')
    if color.lower() == 'quit':
        break
    elif color.lower() == 'pink':
        print('I love this color')
        break
    else:
        print('this one is nice too')
        break


#Написати 3 приклади з continue у середини.

#1

for i in range(10):
    if i == 5:
        print("Returning to the top of the loop!")
        continue
    print(i)



#2
x = 10
while x:
    x = x - 1
    if x % 2 != 0:
        continue
    print(x, "", end='')



#3

new_var = 8
while new_var > 0:
    new_var = new_var - 1
    if new_var == 3: #  skip the part of the loop
        continue
    print(new_var)
print("loop end")
   
    
#4 Написати приклади усіх методів з set().    
    
#1 add/remove

names = {"Steve", "Rick", "Volodymir"}
names2 = names
names2.add("Dmitro")
names.remove("Volodymir")
print("Old Set is:", names)
print("New Set is:", names2)

#2 set.difference
fruits = {"apple", "banana", "cherry"}
veggies = {"potato", "spinach", "carrot","cherry"}

diffSet = fruits.difference(veggies)

print(diffSet)


#3 pop
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#4 discard
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#4 union
fruits  = {"apple", "banana", "cherry"}
veggies = {"potato", "spinach", "carrot","cherry"}

diffSet = fruits.union(veggies) 

print(diffSet)

#5 update

fruits = {"apple", "banana", "cherry"}
veggies = {"potato", "spinach", "carrot","cherry"}
fruits.update(veggies)
print(fruits)



#Задача 1. 10 баллов
#пользователь вводит пароль первый раз система запоминает и просит повторить пароль проверяет его если нет то просит повторить. А если совпал то сообщение.
while True:
    p = input("Input your password")
    x = input("Input your password again")
    if p == x:
        print("Valid Password")
        break
    elif p != x:
        print("not true, please try again")

#Задача_2. 5 баллов
#Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
#Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
#Результат: ['bear', 'milk']

products = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
extra_element = 'eg'
while extra_element in products:
    products.remove('eg')
print(products)




#Задача_3. 10 баллов
#Тема while and else
#дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
#Пример входных данных: [11, 23, 65, 44, 76, 533]
#Результат: NO
#Пример входных данных: [12, 22, 66, 44, 76, 534]
#Результат: all numbers are even

sp_sp = [12, 4, 66, 44, 76, 534]
i = 0
f = 0
while i < len(sp_sp):
  f = f + sp_sp[i] % 2
  i = i+1
if f == 0:
    print("all numbers are even")
else:
    print("No")




#Задача_4 25 баллов
#написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается
#методы без подчеркиваний. Фунции dir()
#т.е для объекта set должен быть список методов

#['add',
#'clear',
#'copy',
#'difference',
#'discard',
#'intersection',
#'isdisjoint',
#'issubset',
#'issuperset',
#'pop',
#'remove',
#'union',
#'update']

sp_sp = dir(set)
f1 = []
for i in sp_sp:
    if i[0] != '_':
        f1.append(i)
print(f1)

#Задача_5 15 баллов
#lis + tuple
#Прочитать статью и сдать тесты в конце статьи
https://realpython.com/quizzes/python-lists-tuples/results/?t=eyJjIjo0LCJuIjoxMSwicSI6Nywic2lnIjoiIUZKZ1pFQHc5az1iPiZRQEJOSihMMUY3VXMtcSF8SUFSK2wlKExqbiIsInQiOjIzNjIwLCJ2IjozfQ==&s=1
#Set
#прочитать статью и пройти на отлично тест в конце.
https://realpython.com/quizzes/python-sets/results/?t=eyJjIjo1LCJuIjoxMCwicSI6MTEsInNpZyI6IkU7fm1tQzJ1RGBMNClhQDM9dCUxYm12X3JuaWhsKSt3Sm0pc2dtQ0wiLCJ0IjoxNTA5MCwidiI6M30=&s=1

#Задача_6 5 балллов﻿
#Написать примеры всех методов из set объекта.
#Пример
#set1 = {1,2,3}
# add
#set1.add(4)
# update
#set1.update([2,3,4,5])

set1 = {1,2,3}
# add
set1.add(4)

# update
set1.update([2,3,4,5])
s = {1, 2, 3}
s.add(5)
print(s)

# clear
s1 = {1, 2, 3}
s1.clear()
print(s1)

# copy
s2 = {1, 2, 3}
s3 = s2.copy()
print(s3)

# symmetric_difference
one = {1, 2, 3}
two = {5, 6, 4, 1, 2, 3}
print(two.symmetric_difference(one))

# discard
s6 = {1, 2, 3}
s6.discard(2)
print(s6)

#isdisjoint
one = {1, 2, 3}
two = {5, 6, 4, 1, 2, 3}
print(two.isdisjoint(one))

# intersection
one = {1, 2, 3, 4}
two = {2, 3, 4, 5}
three = {3, 4, 5, 6}
four = {4, 5, 6, 7}
result = one.intersection(two,three,four)
print(result)

# discard
s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3, 7}
s4.discard(1)
print(s4)

# union
one = {1, 2, 3}
two = {5, 6, 4, 1, 2, 3}
print(one.union(two))

#update
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
x1.update(['corge', 'garply'])
print(x1)

#remove
s4 = {1, 2, 3}
s5 = {5, 6, 4, 1, 2, 3, 7}
s4.remove(1)
print(s4)

   
    
