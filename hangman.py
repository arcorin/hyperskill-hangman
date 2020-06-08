import random
import string

# Stage 8/8

def play_game():
    words_list = ['python', 'java', 'kotlin', 'javascript']
    computer_word = random.choice(words_list)
    computer_word_ = ""

    for x in range(len(computer_word)):
        computer_word_ += "-"
    guessed_letters = []
    wrong_letters = []
    count = 8

    while count > 0:    
        print()
        print(computer_word_)
        letter = input("Input a letter:")
        
        if len(letter) != 1:
            print("You should input a single letter")
            
        elif letter not in string.ascii_lowercase :
            print("It is not an ASCII lowercase letter")
        
        elif letter in guessed_letters or letter in wrong_letters:
            print("You already typed this letter")
        
        elif letter in computer_word:
            guessed_letters.append(letter)
            computer_word_ = ""
            
            for a in computer_word:
                if a in guessed_letters:
                    computer_word_ += a
                else:
                    computer_word_ += "-"
            
        elif letter not in computer_word:
            wrong_letters.append(letter)
            print("No such letter in the word")
            count -= 1
        
        if computer_word_ == computer_word:
            print("You guessed the word!")
            break     
        
    print("You survived!" if computer_word_ == computer_word else "You are hanged!")

print("H A N G M A N")
play_choice = input('Type "play" to play the game, "exit" to quit:')

if play_choice == "play":
    play_game()
else:
    exit()
