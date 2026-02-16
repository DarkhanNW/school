# Kevin Michael P. Lee, 242539
# February 9, 2026

# I certify that this submission complies with the DISCS Academic Integrity
# Policy and the specifications of this course requirement.

# If I have discussed my Python language code with anyone other than
# my instructor(s), my groupmate(s), the teaching assistant(s),
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my program.

# If any Python language code or documentation used in my program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website, genaI tool, or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my program.

################################################################################

# Cite your sources here, if any.
# No need for any formal citation format.
# If use of GenAI tools is allowed for this requirement, 
#   please provide either a list of the prompts used
#   or a link to the conversation.

################################################################################

def char_lister(list): # Returns a list as a string.
    string = ""
    for char in list:
        string += char
    return string

def char_list_updater(list, guess): # Returns a new list of characters, sans the guessed character.
    new_list = []
    for char in list:
        if guess == char:
            continue
        else:
            new_list.append(char)
    return new_list

def guess_validator(list, guess): # Returns True if the guess is part of a list.
    for char in list:
        if guess == char:
            return True
    return False

def guess_checker(guess, guess_word, word): # Checks if the guess is correct.
    new_guess_word = ""
    count = 0
    for char in word:
        if guess == char:
            new_guess_word += guess
            count += 1
        else:
            new_guess_word += guess_word[count]
            count += 1
    return new_guess_word # new_guess_word will be the same as guess_word if the guess is incorrect.

def main():
    print("LET'S PLAY HANGMAN!")
    guess_word = ""
    word = input("Please enter a word for the other player to guess: ").upper()
    valid_char_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    char_list = valid_char_list
    num_guesses = 6
    guess_word += "-" * len(word)
    while guess_word != word:
        if num_guesses <= 0:
            print(f"\nGuess the word, {num_guesses} guess(es) left: {guess_word}\nUnused letters: {char_lister(char_list)}\nSORRY, YOU ARE HANGED!")
            break
        guess = input(f"\nGuess the word, {num_guesses} guess(es) left: {guess_word}\nUnused letters: {char_lister(char_list)}\n").upper()

        if guess_validator(valid_char_list, guess) == False:
            print("\nPlease choose a valid letter.")
            continue
        elif guess_validator(valid_char_list, guess) == True and guess_validator(char_list, guess) == False:
            print("\nYou have already used that letter.")
            continue

        guess_word_check = guess_checker(guess, guess_word, word)
        char_list = char_list_updater(char_list, guess)
        if guess_word == guess_word_check: # checks if guess is correct: -1 guess if it's not.
            num_guesses -= 1
        guess_word = guess_word_check

    if guess_word == word:
        print(f"\nGuess the word, {num_guesses} guess(es) left: {guess_word}\nUnused letters: {char_lister(char_list)}\nCONGRATULATIONS! YOU WIN!")
    
main()