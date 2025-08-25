import string

def shift_letter(letter, shift):
    list_of_letters = list(string.ascii_uppercase)
    if letter == " ":
        return " "
    new_letter_index = list_of_letters.index(letter) + shift
    if new_letter_index >= 26:
        new_letter_index = new_letter_index % 26
        return list_of_letters[new_letter_index]
    return list_of_letters[new_letter_index]

print(shift_letter(" ", 1))
for len in range(0, 27):
    print(shift_letter("B", len))