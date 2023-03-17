#Data types

#String
print("Hello"[0]) #Extrair um caractér de uma string é chamado de subscripting.

#Integer (Número inteiros)
print(123 + 345)

123_456_789 #Usar underline para separar as casas decimais, isso é ignorado pelo sistema.

#Float (Número decimais)
3.14159

#Boolean
True
False

#Data type conversion
num_char = len(input("What is your name?\n"))
new_num_char = str(num_char) #A função str converte um dado em string.
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a)) #função type identifica o tipo de dado.

print(70 + float("100.5"))
#A função float converte um dado para um float.