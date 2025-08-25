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

def caesar_cipher(message, shift):
    pass

def shift_by_letter(letter, letter_shift):
    list_of_letters = list(string.ascii_uppercase)
    if letter == " ":
        return " "
    new_letter_index = list_of_letters.index(letter) + list_of_letters.index(letter_shift)
    if new_letter_index >= 26:
        new_letter_index = new_letter_index % 26
        return list_of_letters[new_letter_index]
    return list_of_letters[new_letter_index]

def main():
    pass

if __name__ == "__main__":
    main()