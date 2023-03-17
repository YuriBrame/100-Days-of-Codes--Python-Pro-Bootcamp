from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caeser(start_text, shift_amount, direction_type):
    result = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if direction_type == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = index + shift_amount
            result += alphabet[new_index]
        else:
            result += char
    print(f"The {direction_type}d message is {result}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caeser(start_text=text, shift_amount=shift, direction_type=direction)

    end_or_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if end_or_continue == "no":
        should_continue = False
        print("Goodbye.")