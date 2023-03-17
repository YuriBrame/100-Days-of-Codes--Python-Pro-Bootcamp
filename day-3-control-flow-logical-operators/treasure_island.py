print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Ilha de Visa.")
print("Sua missão é encontrar o Culto.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input('Vocês atracaram na baia inicial, vocês seguem o rio ou montam acampamento? Digite "Rio" ou "Acampar".\n').lower()

if choice1 == "rio":
    choice2 = input('Vocês seguem o rio e são emboscados por um bando de velociraptos, vocês lutam ou correm? Digite "Lutar" ou "Correr".\n').lower()
    if choice2 == "lutar":
       print("Vocês são devorados pelos velociraptors. Fim de jogo")
    if choice2 == "correr":
        choice3 = input('Vocês escapam dos velociraptors e encontram grandes ruínas antigas mais adiante. Já está anoitecendo, vocês entram nas ruínas ou montam acampaento? Digite "Entrar" ou "Acampar".\n').lower()
        if choice3 == "entrar":
            print('Vocês adentram as misteriosas ruínas e lá dentro encontram os restos mortais do culto, eles parecem ter se matado. Vocês Venceram!')
        if choice3 == "acampar":
            print("Vocês montam acampamento na entrada das ruínas e começam a descansar. Durante a noite vocês são atacados por fantasmas, eles sobrepujam e matam vocês. Fim de Jogo!")
if choice1 == "Acampar":
    print()


        