import random


def read_words(filename='20k.txt'):
    ''' Read file of most popular english words'''
    with open(filename) as words_file:
        words = words_file.read()
    words = [word for word in words.split('\n') if
             len(word) > 5]
    return words


def choose_random_word(words):
    ''' Choose random word from list '''
    return random.choice(words)

print(choose_random_word(read_words()))
word = choose_random_word(read_words())
print(word)
guesses = 8
alfabetic = 'abcdefghijklmnopqrstuvwxyz'

print('Welcome to the game, Hangman!')
print('I am thinking of a word that is %d letters long.' % len(word))
print('____________')
print('You have %d guesses left' % guesses)
print(alfabetic)






