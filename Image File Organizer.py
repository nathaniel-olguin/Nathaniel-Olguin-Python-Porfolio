#PROJECT:    File Organizer
#    -    Import the os module.
#    -    Move files into folders by file type (e.g., .jpg → “Images”).
#SKILLS:    This uses loops, conditionals, imports, and practical applications
#NOTES:    decided to make this for image file types specifically. 


#IMPORTS
import os


#STEP 1 - Obtain starting directory and assign to variable
initial_directory = os.getcwd()
initial_directory_list = os.listdir(os.getcwd())
print(initial_directory)


#STEP 2 - Creating image file type folders
os.makedirs('Organized Images\\PNG', exist_ok=True)
image_types = os.chdir('Organized Images')    #update current directory to the newly created folder 'Organized Images'
os.makedirs('JPEG', exist_ok=True)
os.makedirs('SVG', exist_ok=True)
os.makedirs('GIF', exist_ok=True)
os.makedirs('WebP', exist_ok=True)
os.makedirs('HEIF', exist_ok=True)
os.makedirs('TIFF', exist_ok=True)
os.makedirs('BMP', exist_ok=True)
os.makedirs('PSD', exist_ok=True)
os.makedirs('PDF', exist_ok=True)
os.makedirs('RAW', exist_ok=True)
os.makedirs('EPS', exist_ok=True)
os.makedirs('AI', exist_ok=True)
os.makedirs('INDD', exist_ok=True)
os.makedirs('DWG', exist_ok=True)


#STEP 3 - switch back to initial directory to verify file types
os.chdir(initial_directory)    #return to the initial directory 
while len(initial_directory_list) > 0:
    file_name = initial_directory_list.pop(0)
    print()
    print(file_name)
    if os.path.exists(file_name):    #verifying the file exists
        print(True)
        print(f'File Size:  {os.stat(file_name).st_size}')
        #verify image file type
        if '.png' in file_name:
            print('File Type:  PNG')
        elif '.jpg' in file_name:
            print('File Type:  JPG')
            
    else:
        print('File Type:  ***Ignored by this program (only looking for image file types)')
    

#STEP 4 - NOT FINISHED YET
print()
print(initial_directory_list)
print()
print(image_types)
