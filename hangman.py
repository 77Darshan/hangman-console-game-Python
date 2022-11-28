import random
import time

name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck!")
time.sleep(2)
print("The game will begin shortly!\n Let's play Hangman!")
time.sleep(3)
#variables needed
def main():
    """In main() all the global variables are mentioned as they will be used further in the code, and word_to_guess list holds
    the possible words that user may encounter in the game, randomly a word from the word_to guess list will be taken. """
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global store_word
    words_to_guess = ["sunday","aspect","marketing","hair","promise","kids","lungs","year","great","diamond","january"]
    word = random.choice(words_to_guess)
    store_word=word[:]
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    
def play_loop():
    """This function keeps the game alive, as allows user to start a new game by entering choice Y(i.e Yes)"""
    global play_game
    play_game = input("Do You want to play againn? y = yes, n = no \n")
    if (play_game == "y" or play_game == "Y"):
        main()
        hangman()
    elif (play_game == "n" or play_game == "N"):
        print("Thanks For Playing! Hope you enjoyed it!")
        exit()
    elif (play_game != "Y" or play_game != "y" or play_game != "N" or play_game != "n"):
        play_loop()
    
# All conditions required for the game
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("Here's your "+str(len(word))+" Letter Hangman Word: " + display +" Enter your guess: \n")
    guess = guess.strip()
    # for making user enter only one character
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    
    elif guess in word:
        """ stores the rightly guessed letter in already_guessed list, and changes the index with guessed letter.
        stores the value returned by find() method in index variable and than add the correctly guessed word to its position"""
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    elif guess in already_guessed:
        print("Try another letter.\n")
    else:
        #This will show the nummber of wrong attempts in graphical form.
        count += 1
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess! " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess! " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess! " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess! " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("Wrong guess! You are hanged!!!\n")
            #print("The word was:",already_guessed,word)
            print("THe Word was: ",store_word)
            play_loop()
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()
main()
hangman()
