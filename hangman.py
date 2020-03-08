import nltk

from nltk.corpus import words
word_list = words.words()

import random, time

def word_creator(l):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string = ""
    count = 0  
    while string not in word_list:
        string = ""
        while len(string) < int(l):
            string += alphabet[random.randint(0,len(alphabet)-1)]
        count += 1
        if count > 2000:
            break
    else:
        return string

def find_indices_of_via_enumerate(char, in_string):
    return list(index for index, c in enumerate(in_string) if char == c)

def play_hangman():
    l = input('What length word would you like to play with?')
    word_chosen = None
    while word_chosen is None:
        word_chosen = word_creator(l)
    else:
        time.sleep(5)
        print('The word has been chosen. Ready or not, here we go.')
        list_of_chosen_letters = []
        for i in range(6):
            letter = input()
            list_of_chosen_letters.append(letter)
            if letter in word_chosen:
                print(letter,find_indices_of_via_enumerate(letter,word_chosen))
            else:
                print("Oh no. %s tries left" %(5-i))
            if all(l in list_of_chosen_letters for l in word_chosen):
                print('You won')
                break
            elif (i == 5):
                print('The word was ' + word_chosen)

def run():
    play_hangman()

if __name__ == "__main__":
    run()