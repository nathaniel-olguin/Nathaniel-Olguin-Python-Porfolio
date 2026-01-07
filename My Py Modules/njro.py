#NATHANIEL JOEL RAY OLGUIN   |   This is my Module of functions that i've built for me


#IMPORTS
from datetime import datetime


#FUNCTIONS   |   TEXT RELATED TOOLS
def timestamp_checker(file):    #***used in the word & character count functions***
    date = datetime.now()    #used for simple_date formatting
    simple_date = date.strftime('%m-%d-%Y')    #used for locating timestamps
    timestamp_count = file.count(simple_date)
    return timestamp_count


def character_count(file):    #the entry-dating formating is 45-ish (spacing and \n lines) characters long    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(file)
    
    final_count = len(file) - (timestamp_count * round(45.5))    #wordcount - the number of timestamps
    print()    #space
    if timestamp_count > 0:    #if i reuse this function and there is no timestamp count no need to mention it.
        print(f'Journal Entries:      {timestamp_count}')    #number of times a journal entry was made calculated using the count of timestamps
    return f'Character Count:  {final_count}'    #word count


def word_count(file):    #word count of the timestamp is 5    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(file)

    word_list = file.split()    #list of words in file
    final_count = len(word_list) - (timestamp_count * 5)
    print()    #space
    if timestamp_count > 0:    #if i reuse this function and there is no timestamp count no need to mention it.
        print(f'Journal Entries:      {timestamp_count}')
    return f'Word Count:            {final_count}'


def punctuation_checker(word):    #***REQUIRES A STRING ARGUMENT***    Must insert a single string. Utilize a while loop and the .pop() method for lists
    split_word = []    #list that holds each individual character of a word.
    rebuilt_word = []    #list of newly rebuilt words
    word = word.lower()    #set the string argument to lowercase
    
    if word.isalnum() is False:    #checking for punctuation: .isalnum() returns False if punctuation/symbols are detected
        #***Punctuation Detected***
        for char in word:    #loop that places each character of a word into the split_word list in order.
            split_word.append(char)   
        while len(split_word) > 0:    #now go thru each character in the list to see if contains any undesired symbols/punctuation to then rebuild the word without them
            char = split_word.pop(0)    #remove each character from the split_word list for testing
            if char == '&':    #checking for & symbol to replace with string 'and'
                rebuilt_word.append('a')
                rebuilt_word.append('n')
                rebuilt_word.append('d')
                final_word = ''.join(rebuilt_word)    #rebuild the word with the .join() method        

            if char not in ('$', '&', '!',  '@', '#', '^', '*', '(', ')', '_', '+', '=', '"', '~', '`', '[', ']', '{', '}', '|', '?', ',', '\\', '/', '<', '>', ';', '.', ' ', '', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):    #checking for certain punctuation 
                rebuilt_word.append(char)
                final_word = ''.join(rebuilt_word)    #rebuild the word with the .join() method
            
    else:
        #***NO Punctuation Detected***
        final_word = word
    return final_word    #outputs a single word


def word_frequency(file):    #how many times a word is used    |   ***REQUIRES A STRING ARGUMENT***   A sentence/paragraph
    frequency = {}    #dictionary for words used
    word_list = file.split()    #list of words in file
    while len(word_list) > 0:
        word = word_list.pop()    #remove words from word_list     
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
            
        if word in ('-', '--', ':', '::'):    #final clearing of undesired punctuation
            del frequency[word]
            
    print()    #space
    print('Word Frequency Data:')
    for key in frequency:    #print items in dictonary
        print(key , frequency[key])
    print()    #space
    return frequency


def top_words(num, string):    #top 5/10/15/20 used words    |   ***REQUIRES An Integer ARGUMENT  &  the same STRING Argument that you would use for:  word_frequency
    words = word_frequency(string)
    print(words)    #DEV REF
    top_word = None

    print()    #space
    num_list_items = list(words.items())
    num_list_values = list(words.values())
    print(num_list_items[0][1])   #DEV REF
    print()
    sort_num_list_values = sorted(num_list_values)
    print(sort_num_list_values)
    


    


#FUNCTIONS   |   DEVELOPER BASICS (simple repeatable stuff for working in the pythong shell)
def line():
    print('''
——————————————————————————————————
''')
