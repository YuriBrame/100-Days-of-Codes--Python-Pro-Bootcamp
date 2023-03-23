programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Recuperando itens de um dicionário.
# print(programming_dictionary["Bug"])

#Adicionando novos items ao dicionário.
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

#Criando um dicionário vazio.
empty_dictionary = {}

#Limpando um dicionário existente.
# programming_dictionary = {}
# print(programming_dictionary)

#Editando items em um dicionário
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

#Usando loops em um dicionário.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])