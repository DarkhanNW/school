# Kevin Michael P. Lee, 242539
# February 16, 2026

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

def char_lister(list, string="", count=0): # Returns a list as a string.
    if count == len(list):
        return string
    string += str(list[count])
    return char_lister(list, string, count+1)

def char_list_updater(list, guess, new_list, count=0): # Returns a new list of characters, sans the guessed character.
    if count == len(list):
        return new_list
    char = list[count]
    if guess == list[count]:
        return char_list_updater(list, guess, new_list, count+1)
    new_list.append(char)
    return char_list_updater(list, guess, new_list, count+1)
    
def guess_validator(list, guess, count=0): # Returns True if the guess is part of a list.
    if count == len(list):
        return False
    if guess == list[count]:
        return True
    return guess_validator(list, guess, count+1)

def guess_checker(guess, guess_word, word, new_guess_word="", count=0): # Checks if the guess is correct.
    if count == len(word):
        return new_guess_word
    if guess == word[count]:
        new_guess_word += guess
    else:
        new_guess_word += guess_word[count]
    return guess_checker(guess, guess_word, word, new_guess_word, count+1)

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
        new_list = []
        char_list = char_list_updater(char_list, guess, new_list)
        if guess_word == guess_word_check: # checks if guess is correct: -1 guess if it's not.
            num_guesses -= 1
        guess_word = guess_word_check

    if guess_word == word:
        print(f"\nGuess the word, {num_guesses} guess(es) left: {guess_word}\nUnused letters: {char_lister(char_list)}\nCONGRATULATIONS! YOU WIN!")
    
main()