import random 
from colorama import Fore, Style, init

init(autoreset=True)

# ASCII-art
HANGMAN_PICS = [
  f"{Fore.RED}" + """
    -------
     |    |
     |
     |
     |
     |
     |
   --------  
    """,
   f"{Fore.RED}" + """
    -------
     |    |
     |    O
     |
     |
     |
     |
   -------- 
    """,
   f"{Fore.YELLOW}" + """
    -------
     |    |
     |    O
     |    |
     |
     |
     |
   -------- 
    """,
   f"{Fore.YELLOW}" + """
    -------
     |    |
     |    O
     |   /|
     |
     |
     |
   -------- 
    """,
   f"{Fore.YELLOW}" + """
    -------
     |    |
     |    O
     |   /|\\
     |
     |
     |
   -------- 
    """,
   f"{Fore.RED}" + """
    -------
     |    |
     |    O
     |   /|\\
     |   /
     |
     |
   -------- 
    """,
   f"{Fore.RED}" + """
    -------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
     |
   -------- 

   """
]

def load_words(filename="words.txt"):
    # Reads the words from a file
    try:
        with open(filename, "r") as file:
            words = file.readlines()
        return [word.strip().lower() for word in words if word.strip()]
    except FileNotFoundError:
        print(f"{Fore.YELLOW}File'{filename}'was not found, using standard words.")
        return ["cat", "computer", "dog"] 
    
def display_word(word, guessed_letters):
    # Shows the word with _ for letters not guessed yet
    return " ".join([f"{Fore.GREEN}{letter}" if letter in guessed_letters else f"{Fore.CYAN}_" for letter in word])

def hangman():
    print(f"{Fore.MAGENTA}Welcome to Hangman!")
    word_list = load_words()
    word = random.choice(word_list)
    guessed_letters = set()
    attempts = len(HANGMAN_PICS) - 1
    guessed = False

    while attempts > 0 and not guessed:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - attempts])
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"{Fore.BLUE}You have {Fore.YELLOW}{attempts} {Fore.BLUE}attempts left.")
        guess = input(f"{Fore.CYAN}Guess a letter or the whole word: {Fore.RESET}").lower()

        if not guess.isalpha() or len(guess) < 1:
            print(f"{Fore.RED}Please enter a valid letter or word.")
            continue

        if guess == word:
            guessed = True
        elif len(guess) == 1:
            if guess in guessed_letters:
                print(f"{Fore.RED}You've already guessed'{guess}'.")
            elif guess in word:
                print(f"{Fore.GREEN}Good job'{guess}' is in the word!")
                guessed_letters.add(guess)
                if all (letter in guessed_letters for letter in word):
                    guessed = True
            else:
                print(f"{Fore.RED}Sorry'{guess}' is not in the word.")
                guessed_letters.add(guess)
                attempts -= 1

        else: 
            print(f"{Fore.RED}'{guess}' is not the right word!")
            attempts -= 1

    if guessed:
        print(f"{Fore.GREEN}Congratulations! You guessed the right word: {Fore.YELLOW}{word}")
    else:
        print(HANGMAN_PICS[-1])
        print(f"{Fore.RED}Sorry, you lost. The correct word was{Fore.YELLOW}'{word}'.")

if __name__ == "__main__":
    hangman()
          
      
    