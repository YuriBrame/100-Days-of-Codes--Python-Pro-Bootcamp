#Listas são basicamente a versão de array do python.

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

#É possível acessar a lista de trás pra frente utilizando números negativos. Começa a partir do -1
# print(states_of_america)

# #Adicionando itens em uma lista. Utilizando a função.append
# states_of_america.append("Angelaland")
# print(states_of_america)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Tomatoes", "Cherries", "Pears", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])