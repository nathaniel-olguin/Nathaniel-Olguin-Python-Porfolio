#⭐️ analysis.py ⭐

#Handles:
#    reading the text
#    analyzing it
#    returning results
#    saving a report into reports


#IMPORTS
import os, njro    #njro is my personal module of functions
from datetime import datetime    #used for finding the current days journal entry


#VARIABLES
date = datetime.now()    #used for simple_date formatting
simple_date = date.strftime('%m-%d-%Y')

initial_directory = os.getcwd()    #reference
data_dir = f'{initial_directory}\\Data'    #directory that holds the files analysis.py will read
data_dir_list = os.listdir(data_dir)


#STEP 1  |  Read the current days journal 'Data' entry
todays_entry = f'Daily Journal  -  {simple_date}.md'

if todays_entry in data_dir_list:    #program looks for todays journal entry
    print('File Exists:  True')
    with open(f'{data_dir}\\{todays_entry}', 'r') as data:
        content = data.read()
else:
    print('File Exists:  False')
print(content)    #Dev Reference


#STEP 2  |  Anaylize the 'content'
njro.line()    #DEV READABILITY
print(njro.character_count(content))
print(njro.word_count(content))

listed_words = content.split()    #turns the content into a list
revised_words = []    #empty list for the end result of the njro.punctuation_checker function
while len(listed_words) > 0:
    word = listed_words.pop()
    revised_words.append(njro.punctuation_checker(word))    #once words are fixed by the function, add to our original empty list
    
revised_words_str = ' '.join(revised_words)    #word_frequency requires a string argument
print(njro.word_frequency(revised_words_str))
njro.line()    #DEV READABILITY
