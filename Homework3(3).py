#task 1
age = 99
user_name ="Ilya"
if  age >= 16 and age <=70:
    print("Welcome"+ user_name)
elif age == 16:
     print("Dear"+ " " + user_name + "," + "you need to wait one year")
elif age > 70 and age < 90:
     print("You are lucky"+ "," + user_name + " " +"and welcome")
elif age > 90:
     print ("You are not real" + " " + user_name)
else:
     print("I am sorry" + " " + user_name)


#task 2
userInput = 0
while True:
  try:
     userInput = int(input("Enter something: "))
  except ValueError:
     print("Not an integer!")
     continue
  else:
     print("Yes an integer!")
     break
if userInput == 21:
        print("You should visit Holland")
elif userInput > 21:
 print("You should visit Vietnam")
else:
 print("Travel everywhere")


























