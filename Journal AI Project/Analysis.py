#⭐️ analysis.py ⭐

#Handles:
#    reading the text
#    analyzing it
#    returning results
#    saving a report into reports



#IMPORTS
from datetime import datetime    #not currently in use


#VARIABLES
initial_directory = os.getcwd()    #reference
data_dir = f'{initial_directory}\\Data'    #directory that holds the files analysis.py will read
data_dir_list = os.listdir(data_dir)


#STEP 1  |  Read the latest journal 'Data' entry
print(data_dir_list)    #reference
if len(data_dir_list) < 2:    #if the 'Data' directory only has 1 entry read that entry
    with open(f'{data_dir}\\{data_dir_list[0]}', 'r') as data:
        content = data.read()
        print(content)
else:    #if the 'Data' directory only has more than 1 entry read the latest(last) entry
    with open(f'{data_dir}\\{data_dir_list[-1]}', 'r') as data:
        content = data.read()
        print(content)
