import nltk

from nltk.corpus import words
#Import words list from above module
word_list = words.words()

import random, time

#Create list for alphabets
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Define function to create words by combining letters and checking if they are proper words
def word_creator(l):
    #Create empty string and countr variable
    string = ""
    count = 0  
    #While the string is not in the word list, do not accept the string and reset to empty string
    while string not in word_list:
        string = ""
        #while string is less than no of letters chosen by user, continue to add a letter to the string at random
        while len(string) < int(l):
            string += alphabet[random.randint(0,len(alphabet)-1)]
        #Increment counter but break if taking too long as words in list incopmrehensibly long
        count += 1
        if count > 2000:
            break
    else:
        return string

#Define function to find index of a letter within a word
def find_indices_of_via_enumerate(char, in_string):
    return list(index for index, c in enumerate(in_string) if char == c)

#Define function to play hangman where it is possible to choose the length of the word to be guessed
def play_hangman():
    #Require user input for length of word
    l = input('What length word would you like to play with?')
    word_chosen = None
    #Use function to create word 
    while word_chosen is None:
        word_chosen = word_creator(l)
    else:
        #Allow for some time after the chosen using the sleep function
        time.sleep(5)
        print('The word has been chosen. Ready or not, here we go.')
        list_of_chosen_letters = []
        wrong_guesses = 0
        #Have a while loop which continues until the threshold for incorrect guesses is reached, allow for user input and reveal whether the lettter guessed is within the word
        while wrong_guesses < 5:
            letter = input()
            list_of_chosen_letters.append(letter)
            if letter in word_chosen:
                print(letter,find_indices_of_via_enumerate(letter,word_chosen))
            else:
                wrong_guesses += 1
                print("Oh no. %s tries left" %(6-wrong_guesses))
            #If all letters found, give a 'you won' message
            if all(l in list_of_chosen_letters for l in word_chosen):
                print('You won')
                break
            #If the thershold is reached, reveal the word
            elif (wrong_guesses == 5):
                print('The word was ' + word_chosen)

def run():
    play_hangman()

if __name__ == "__main__":
    run()