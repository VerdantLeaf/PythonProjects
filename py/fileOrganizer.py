from pathlib import Path
import os
import shutil
from tabulate import tabulate

subdirs = []    # Array of all the names of the current subdirectories
extensions = [] # Array to store all of the file extensions
files = {}

cwd = Path.cwd()

for dir in cwd.iterdir():
    if dir.is_dir() and not dir.name.startswith('.'):
        subdirs.append(dir.name)

# Scan the current dir for all of the extensions
for file_name in os.listdir(cwd):
    filepath = os.path.join(cwd, file_name)
    # See if it is a file or a dir and that it doesn't start with .
    if os.path.isfile(filepath) and not file_name.startswith('.') :

        ext = file_name.split('.') # Split the string at the periods, & grab the final one

        if len(ext) == 1 and not file_name.startswith('.'): # Just don't handle this at the moment
            continue

        ext = ext[-1]

        if ext not in extensions:
            extensions.append(ext)
        
        try:
            print(file_name)
            files[ext].append(file_name)
        except KeyError:
            files.update({ext: [file_name]})

print("Files to organize into subdirectories:")
print(tabulate(files, headers=extensions,  tablefmt='orgtbl'))

key = input("Press Enter to confirm process, any other key to cancel")

if key != '':
    print("Exiting...")
    os._exit(0)


# # make the new directories
for extension in extensions:
    dir = Path(extension)
    dir.mkdir(exist_ok= True)

    for file_name in files[extension]:
        filepath = os.path.join(cwd, file_name)
        try:
            shutil.copy(filepath, os.path.join(cwd, extension)) # Just copy things over for now
        except FileExistsError:
            # Handle the case when the file already exists - Remove or append # to file name?
            continue


    
