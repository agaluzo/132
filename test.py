import random


def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if
             len(word) > 5]
    return words


def choose_random_word(words):
    """ Choose random word from list """
    return random.choice(words)


def display_available_letters(alphabet, letter):
    available_letters = alphabet.replace(letter, "")
    return available_letters


def display_guessed_word(word, guessed_word, letter):
    new_guessed_word = guessed_word
    for i in range(0, len(word)):
        if word[i] == letter:
            new_guessed_word = new_guessed_word[0:i] + letter + new_guessed_word[i+1:]
    return new_guessed_word

word = choose_random_word(read_words())
print(word)
guessed_word = ''.ljust(len(word), '_')
print(guessed_word)
guesses = 8
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print('Welcome to the game, Hangman!')
print('I am thinking of a word that is %d letters long.' % len(word))
print('____________')

while guesses != 0:
    print('You have %d guesses left' % guesses)
    print('available letters: %s' % alphabet)
    letter = input('Please guess a letter: ')
    alphabet = display_available_letters(alphabet, letter)
    guessed_word = display_guessed_word(word, guessed_word, letter)
    if word == guessed_word:
        print("winner")
        break
    elif letter in guessed_word:
        print("Good guess: " + guessed_word)
    else:
        print("Oops! That letter is not in my word: " + guessed_word)
        guesses -= 1


print("you loose")