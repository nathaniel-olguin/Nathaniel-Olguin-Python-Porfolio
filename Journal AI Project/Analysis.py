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
specific_time = date.strftime('%m-%d-%Y  -  %A, %I:%M:%S %p')    #specific datetime for each new entry within the file

initial_directory = os.getcwd()    #reference
data_dir = f'{initial_directory}\\Data'    #directory that holds the files analysis.py will read
data_dir_list = os.listdir(data_dir)
report_dir = f'{initial_directory}\\Reports'    #directory for reports
report_dir_list = os.listdir(report_dir)


#STEP 1  |  Read the current days journal 'Data' entry
todays_entry = f'Daily Journal  -  {simple_date}.md'

if todays_entry in data_dir_list:    #program looks for todays journal entry
    with open(f'{data_dir}\\{todays_entry}', 'r') as data:
        content = data.read()
else:
    pass


#STEP 2  |  Anaylize the 'content'
character_count = njro.character_count(content)
word_count = njro.word_count(content)
revised_content = njro.punctuation_checker(content)[1]    #returns a list of cleaned up words
main, filler = njro.word_frequency(revised_content)    #how often a word is used
top_main, top_filler = njro.top_words(revised_content)    #top 3 most used main & filler words
sentiment = njro.sentiment(revised_content)    #emotional tone of the text


#STEP 3   |   Creating a report of the 'content'
todays_report = f'Daily Report  -  {simple_date}.md'

with open(f'{report_dir}\\{todays_report}','a') as report:
    report.write(f'''
#{specific_time}

    ###Character Count:
        {character_count}
        
    ###Word Count:
        {word_count}
{njro.line(1)}
    ###Words Used:
        {main}

    ###Filler Words Used:
        {filler}
{njro.line(1)}
    ###Top Words used:
        {top_main}

    ###Top Filler Words Used:
        {top_filler}
{njro.line(1)}
    ###Sentiment:
        {sentiment}
{njro.line(1)}''')    #END      
