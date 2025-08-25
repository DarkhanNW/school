import string

list_uppercase_letters = list(string.ascii_uppercase)

def shift_letter(letter, shift):
    if letter == " ":
        return " "
    new_letter_index = list_uppercase_letters.index(letter) + shift
    if new_letter_index >= 26:
        new_letter_index = new_letter_index % 26
        return list_uppercase_letters[new_letter_index]
    return list_uppercase_letters[new_letter_index]

def caesar_cipher(message, shift):
    list_message = list(message)
    list_new_message = []
    for letter in list_message:
        list_new_message.append(shift_letter(letter, shift))
    new_message_joined = "".join(list_new_message)
    return new_message_joined

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    new_letter_index = list_uppercase_letters.index(letter) + list_uppercase_letters.index(letter_shift)
    if new_letter_index >= 26:
        new_letter_index = new_letter_index % 26
        return list_uppercase_letters[new_letter_index]
    return list_uppercase_letters[new_letter_index]

def main():
    pass

if __name__ == "__main__":
    main()