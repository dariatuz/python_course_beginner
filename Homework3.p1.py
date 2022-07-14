# задание 0: objects
# строки
string_one = 'My first string'
print(string_one)
string_two = 'My second string'
print(string_two)
string_three = 'My third string'
print(string_three)

# списки
dogs_list = [ 'Kai', 'Butcher', 'Cookie', 'Ginger']
print(dogs_list)
cats_list = ['Bella', 'Murka', 'Demogorgon']
print(cats_list)
students_list = ['Ivan', 'Masha', 'Dasha']
print(students_list)

#числа(с плавающей точкой, целочисленные)
floating_first = 25.1
print(floating_first)
floating_second = 3.21
print(floating_second)
floating_third = 6.66
print(floating_third)

intg_one = 25
print(intg_one)
intg_two = 789384
print(intg_two)
intg_three =44448960
print(intg_three)

#словари
kitchen_utensils = {1: "fork", 2: "knife", 3: "spoon"}
print(kitchen_utensils)
furniture = {125:"sofa", 126:"table", 127:"bed"}
print(furniture)
ex_boyfriends = {115:"Misha",123:"Vlad",444:"Ahmed" }
print(ex_boyfriends)

#кортежи
tuple_one = (1, 2, 3, 4, 5, 6)
print(tuple_one)
name_and_age = ('Lana', 22, 'Daria', 28)
print(name_and_age)
letters_list = ('c', 'o', 'd', 'e', 'c', 'h', 'i', 'c', 'k')
print (letters_list[0])


# max(), min()
numbers_list = [5, 8, 9, 4, 10, 6]
largest_number = max(numbers_list)
print("The largest number is:", largest_number)

numbers_min = [1, -1, 3]
min_number = min(numbers_min)
print("The smallest number is:", min_number)

supplier_prices = [3.66, 182, 3, 3.30, 3.32, 3.26]
print("The cheapest price is $", min(supplier_prices),"per kilo of beef")

supplier_prices = [3.66, 182, 3, 3.30, 3.32, 3.26]
print("The highest price is $", max(supplier_prices),"per kilo of beef")

grades = "ACCCCCCD"

print("The lowest grade in the class was", min(grades))

grades = "ACCCCCCD"

print("The highest grade in the class was", max(grades))



#оператор in

existing_number = 3 in [3, 4, 5, 8]
print(existing_number)

existing_animals = "panda" in ["panda", "lion", "tiger"]
print(existing_animals)

existing_animals = "panda" in ["panda", "lion", "tiger"]
print(existing_animals)

grades = "D" in "ABCD"
print("D")

#if elif else
speed = 130
if speed > 120:
    print("Dangerous, slow down")
elif num == 100:
    print("Good, speed is normal")
else:
    print("Maybe you should speed up?")

dogs = 3
if dogs > 300:
    print("Maybe we should stop buying dogs")
elif dogs == 3:
    print("We have enough pets at home")
else:
    print("Maybe you should buy a dog?")

price = 656
quantity = 4

if price*quantity > 800:
    print("price is greater than 800")
elif price*quantity == 0:
    print("Zero")
else:
    print("Negative number")









