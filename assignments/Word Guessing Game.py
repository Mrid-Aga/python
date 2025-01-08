import random
words = ["attention","prove","part","mirror"]
chosen_word = random.choice(words)
user_word = "*"*len(chosen_word)
guesses = len(chosen_word)+2
hangman_count = 0
guessed_letters = []
def hangman():
    if hangman_count == 0:
        print("  ____")
        print(" |    |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 1:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 2:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |    |")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 3:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 4:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 5:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   /")
        print(" |")
        print(" |")
        print("_|_")
    elif hangman_count == 6:
        print("  ____")
        print(" |    |")
        print(" |    O")
        print(" |   /|\\")
        print(" |   / \\")
        print(" |")
        print(" |")
        print("_|_")
print(user_word)
hangman()
while user_word != chosen_word and guesses >0 and hangman_count != 6:
    user_input = input("Guess a letter: \n")
    guesses -= 1
    user_input = user_input.lower()
    if user_input in chosen_word and user_input not in guessed_letters:
        for i in range(len(chosen_word)):
            user_word = list(user_word)
            if chosen_word[i] == user_input:
                user_word[i] = user_input
    elif user_input in chosen_word:
        print(f"You've already guessed {user_input}")
        guesses += 1
    else:
        print("Sorry, that's not part of the word")
        hangman_count += 1
        hangman()
        user_input
    if user_input not in guessed_letters:
        guessed_letters.append(user_input)
    elif user_input in guessed_letters and user_input in chosen_word:
        print("You've already guessed that, it's correct")
    elif user_input in guessed_letters and user_input not in chosen_word:
        print("you've already guessed that, it's not part of the word")
    user_word = "".join(user_word)
    guessed_letters.sort()
    print(user_word)
    print(f"You have {guesses} guesses left")
    print(f"You have guessed {guessed_letters} so far")
if user_word == chosen_word and guesses > 0 and hangman_count < 6:
    print(f"Congrats you guessed correctly in just {len(chosen_word)+2-guesses} guesses")
else:
    print(f"Sorry, you couldn't guess the word. The word was {chosen_word}")
    hangman_count = 6
    hangman()