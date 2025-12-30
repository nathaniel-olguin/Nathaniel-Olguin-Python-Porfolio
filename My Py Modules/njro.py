#NATHANIEL JOEL RAY OLGUIN   |   This is my Module of functions that i've built for me


#IMPORTS
from datetime import datetime


#FUNCTIONS
def character_count(file):    #the entry-dating formating is 45-ish (spacing and \n lines) characters long
    date = datetime.now()    #used for simple_date formatting
    simple_date = date.strftime('%m-%d-%Y')    #used for locating timestamps

    timestamp_count = file.count(simple_date)    #counting the amount of times my entry-datetime formatting is present
    final_count = len(file) - (timestamp_count * round(45.5))    #wordcount - the number of timestamps
    print()    #space
    print(f'Journal Entries:      {timestamp_count}')    #number of times a journal entry was made calculated using the count of timestamps
    return f'Character Count:  {final_count}'    #word count

def word_count(file):    #word count of the timestamp is 5
    date = datetime.now()    #used for simple_date formatting
    simple_date = date.strftime('%m-%d-%Y')    #used for locating timestamps

    timestamp_count = file.count(simple_date)
    word_list = file.split()    #list of words in file
    final_count = len(word_list) - (timestamp_count * 5)
    print()    #space
    print(f'Journal Entries:      {timestamp_count}')
    return f'Word Count:             {final_count}'

def word_frequency(file):    #***NEEDS WORK***
    frequency = {}    #dictionary for words used
    word_list = file.split()    #list of words in file
    while len(word_list) > 0:
        word = word_list.pop()    #remove words from word_list     
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
            
    print()    #space
    print('Word Frequency Data:')
    for key in frequency:    #prnt items in dictonary
        print(key , frequency[key])
    print(word_list)    #for dev reference

def punctuation_checker(word):    #Currently ignores: &, integers, hyphens, and apostrophes
    split_word = []    #list that holds each individual character of a word.
    new_word = []    #list of newly rebuilt words
    if word.isalnum() is False:    #checking for punctuation 
        print('***Punctuation Detected')
        for char in word:    #loop that places each character of a word into the split_word list in order.
            split_word.append(char)
            print(split_word)
        #now i need to go thru each item in the list to see if its alpha/num to then rebuild the word without punctuation
        while len(split_word) > 0:
            char = split_word.pop(0)    #remove each character from the split_word list for testing
            if char == '&':    #checking for & symbol to replace with string 'and'
                new_word.append('and')
            else:
                print('No "&" Detected')
            if char not in ('&', '!',  '@', '#', '^', '*', '(', ')', '_', '+', '=', '"', '~', '`', '[', ']', '{', '}', '|', '?', ',', '\\', '/', '<', '>', ':', ';', '.'):    #checking for certain punctuation 
                new_word.append(char)
                print(new_word)            
            else:
                print('***PUNCTUATION FOUND')    
    else:
        print('***NO Punctuation Detected')
        
    final_word = ''.join(new_word)
    return f' ***Word without punctuation:  {final_word}'
