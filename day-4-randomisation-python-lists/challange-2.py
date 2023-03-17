# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.

# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name.

# Import the random module here

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# number_of_people = len(names)
# random_number = random.randint(0, number_of_people - 1)
# chosen_one = names[random_number]

#Método utilizando a função .choice.
chosen_one = random.choice(names)
print(f"{chosen_one} is going to buy the meal today!")
