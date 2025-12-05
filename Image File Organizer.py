#PROJECT:    File Organizer
#    -    Import the os module.
#    -    Move files into folders by file type (e.g., .jpg → “Images”).
#SKILLS:    This uses loops, conditionals, imports, and practical applications
#NOTES:    decided to make this for image file types specifically. When finishing this project I initally thought that the OS module was all that was needed for this project but while researching I discoved that the SHUTIL module would be perfect for completing this project


#IMPORTS
import os
import shutil


#STEP 1 - Obtain starting directory and assign to variable
initial_directory = os.getcwd()
initial_directory_list = os.listdir(os.getcwd())
print(initial_directory)    #for reference


#STEP 2 - Creating image file type folders
os.makedirs('Organized Images\\PNG', exist_ok=True)
os.chdir('Organized Images')    #update initial directory to the newly created folder 'Organized Images'
new_directory = os.getcwd()
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
        #verify image file type then move the file types into the new_directory plus the designated file type folder
        if '.png' in file_name or '.PNG' in file_name:
            print('File Type:  PNG')
            shutil.move(file_name, f'{new_directory}\\PNG')
        elif '.jpg' in file_name or '.JPG' in file_name:
            print('File Type:  JPG')
            shutil.move(file_name, f'{new_directory}\\JPEG')
        elif '.svg' in file_name or '.SVG' in file_name:
            print('File Type:  SVG')
            shutil.move(file_name, f'{new_directory}\\SVG')
        elif '.gif' in file_name or '.GIF' in file_name:
            print('File Type:  GIF')
            shutil.move(file_name, f'{new_directory}\\GIF')
        elif '.webp' in file_name or '.WEBP' in file_name:
            print('File Type:  WebP')
            shutil.move(file_name, f'{new_directory}\\WebP')
        elif '.heif' in file_name or '.HEIF' in file_name:
            print('File Type:  HEIF')
            shutil.move(file_name, f'{new_directory}\\HEIF')
        elif '.tiff' in file_name or '.TIFF' in file_name:
            print('File Type:  TIFF')
            shutil.move(file_name, f'{new_directory}\\TIFF')
        elif '.bmp' in file_name or '.BMP' in file_name:
            print('File Type:  BMP')
            shutil.move(file_name, f'{new_directory}\\BMP')
        elif '.psd' in file_name or '.PSD' in file_name:
            print('File Type:  PSD')
            shutil.move(file_name, f'{new_directory}\\PSD')
        elif '.pdf' in file_name or '.PDF' in file_name:
            print('File Type:  PDF')
            shutil.move(file_name, f'{new_directory}\\PDF')
        elif '.raw' in file_name or '.RAW' in file_name:
            print('File Type:  RAW')
            shutil.move(file_name, f'{new_directory}\\RAW')
        elif '.eps' in file_name or '.EPS' in file_name:
            print('File Type:  EPS')
            shutil.move(file_name, f'{new_directory}\\EPS')
        elif '.ai' in file_name or '.AI' in file_name:
            print('File Type:  AI')
            shutil.move(file_name, f'{new_directory}\\AI')
        elif '.indd' in file_name or '.INDD' in file_name:
            print('File Type:  INDD')
            shutil.move(file_name, f'{new_directory}\\INDD')
        elif '.dwg' in file_name or '.DWG' in file_name:
            print('File Type:  DWG')
            shutil.move(file_name, f'{new_directory}\\DWG')
        else:
            print('File Type:  NOT AN IMAGE TYPE')

    else:
        print('File not found')    #verifying the file exists
    

#STEP 4 - end results
print()
print(initial_directory_list)    #verifying all the files from the initial directory have been viewed
print()
print(new_directory)    #for reference
