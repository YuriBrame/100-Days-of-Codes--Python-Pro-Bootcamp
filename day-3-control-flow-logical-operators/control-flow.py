print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

#elif pode ser utilizado dentro de um if para checar novas condições.

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <=12:
        print("Child tickets are $5.")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12

    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride")

#Operadores de comparação
# > - Maior que
# < - Menor que
# >= - Maior ou igual que
# <= - Menor ou igual que
# == - Igual a
# - != - Não igual a