import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_dictionary)

program_on = True

while program_on:
    word = input("Please enter a word: ").upper()
    if word == "EXIT":
        program_on = False
        break
    letters = [letter for letter in word]

    nato_translation = [nato_dictionary[letter] for letter in word]
    # for letter in letters:
    #     for (key, value) in nato_dictionary.items():
    #         if key == letter:
    #             nato_translation.append(value)

    print(nato_translation)

# #TODOo 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# todoo 2. Create a list of the phonetic code words from a word that the user inputs.
