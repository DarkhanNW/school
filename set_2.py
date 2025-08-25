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

def vigenere_cipher(message, key):
    list_message = list(message)
    list_new_message = []
    list_key = list(key)
    list_key_index = 0
    while len(list_message) > len(list_key):
        list_key.append(list_key[list_key_index])
        list_key_index += 1

    list_key_index = 0
    for letter in list_message:
        list_new_message.append(shift_by_letter(letter,list_key[list_key_index]))
        list_key_index += 1
    new_message_joined = "".join(list_new_message)
    return new_message_joined

def scytale_cipher(message, shift):
    list_message = list(message)
    list_new_message = []
    while len(list_message) % shift != 0:
        list_message.append("_")
    
    for i in range(0, len(list_message)):
        list_new_message.append(list_message
                [
            (i // shift)
            + (len(list_message) // shift)
            * (i % shift)
            ]
        )

    new_message_joined = "".join(list_new_message)
    return new_message_joined

def scytale_decipher(message, shift):
    list_message = list(message)
    new_message = ""
    row_num = 0
    while len(list_message) % shift != 0:
        list_message.append("_")
    
    for i in range(0, shift):
        new_message_part = (list_message[row_num::shift])
        new_message += "".join(new_message_part)
        row_num += 1

    return new_message

def main():
    print(scytale_cipher("INFORMATION_AGE", 3))
    print(scytale_decipher("IMNNA_FTAOIGROE", 3))

if __name__ == "__main__":
    main()