#⭐️ journal.py ⭐️

#Handles:
#	•	getting the text from the user
#	•	saving it into data/entries


#IMPORTS
import os
import shutil
from datetime import datetime


#STEP 1  |  user input
try:
    daily_entry = input()
except EOFError:    #enter with nothing
    daily_entry = ''
finally:
    print(datetime.now())
    for count in range(2):
        print()
    print(daily_entry)
    for count in range(2):
        print()


#STEP 2  |  creating an 'entry file'  |  WORK-IN-PROGRESS
print(os.name)
cwd = os.getcwd
print(cwd)
