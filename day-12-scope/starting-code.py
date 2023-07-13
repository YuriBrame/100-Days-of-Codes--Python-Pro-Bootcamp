################### Scope ####################

# Modifying global scope

enemies = 1

def increase_enemies():
  # É necessário nomear especificamente a variavel global.
  global enemies
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# A convenção de nomes do python é de nomear as constantes globais com com letras maiusculas e dividido por underline.


