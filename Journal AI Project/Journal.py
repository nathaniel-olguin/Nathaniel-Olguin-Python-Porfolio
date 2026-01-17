#⭐️ journal.py ⭐️

#Handles:
#	•	getting the text from the user
#	•	saving it into data/entries


#IMPORTS
import os
from datetime import datetime


#VARIABLES
date = datetime.now()
specific_time = date.strftime('%m-%d-%Y  -  %A, %I:%M:%S %p')    #specific datetime for entries within the file
simple_date = date.strftime('%m-%d-%Y')    #for the file name
initial_directory = os.getcwd()    #reference
data_dir = f'{initial_directory}\\Data'


#STEP 1  |  user input
try:
    daily_entry = input()
except EOFError:    #catches when nothing is entered
    daily_entry = ''


#STEP 2  |  OS module: Creating the directories:  'Reports' & 'Data'
os.makedirs('Reports', exist_ok=True)    #Analysis.py will handle this directory (I might move this line of code into Analysis.py once i start working on that file)
os.makedirs('Data', exist_ok=True)    #This is where the journal entries will be moved too


#STEP 3  |  creating an 'entry file' or adding onto an existing file for the same day
if f'Daily Journal  -  {simple_date}.md' in initial_directory:
    with open(f'{data_dir}\\Daily Journal  -  {simple_date}.md', 'a') as entry:
        entry.write(f'\n \n#{specific_time} \n \n    {daily_entry} TEST')
else:
    with open(f'{data_dir}\\Daily Journal  -  {simple_date}.md', 'a') as entry:    #currently need to fix the 'a' and \n \n at the beginning since currently the initial directory is causeing issues with this if-else block
        entry.write(f'\n \n#{specific_time} \n \n    {daily_entry}')
