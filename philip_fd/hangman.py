import random
from words import words
import string

#words that have spaces cant be guesed

def get_valid_words(words):
    word= random.choice(words) #randomly choose something from the list
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
def hangman():
    word= get_valid_words(words)
    word_letters=set(word)
    alphabet=set(string.ascii_uppercase)
    used_letters=set()

    lives = 10
    while len(word_letters)>0 and lives>0:
        #letters used
        print('you have',lives,' used:', ' '.join(used_letters))

        #what current word is 
        word_list= [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))
            
        used_letter=input('Guess a letter: ').upper()
        if used_letter in alphabet-used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
            else:
                lives = lives-1
                print("letter isnt in word")
        elif used_letter in used_letters:
            print('You have already used that charcter. Please try again')
        else:
            print('invalid character')
    if lives ==0:
        print('you died word was', word)
    else:
        print('you guessed the word ',word, '!!')


hangman()