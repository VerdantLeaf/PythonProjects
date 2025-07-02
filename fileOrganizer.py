from pathlib import Path
import os
import shutil
import regex as re
from tabulate import tabulate

# Purpose: This program looks at the directory it is run in and then organizes the files found within the directory for the user into subdirectories
# whose names are based on the file extension

# Reason: The reason to develop this program was to become more familiar with Python as my experience is spotty and inconsistent

# Author: VerdantLeaf on GitHub

subdirs = []    # Array of all the names of the current subdirectories
extensions = [] # Array to store all of the file extensions
files = {}

cwd = Path.cwd()

for directory in cwd.iterdir():
    if directory.is_dir() and not directory.name.startswith('.'):
        subdirs.append(directory.name)

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
            files[ext].append(file_name)
        except KeyError:
            files.update({ext: [file_name]})

print("Files to organize into subdirectories:")
print(tabulate(files, headers=extensions,  tablefmt='orgtbl'))

key = input("Press Enter to confirm process, any other key to cancel\t")

if key != '':
    print("Exiting...")
    print()
    os._exit(0)


# # make the new directories
for extension in extensions:
    directory = Path(extension)
    directory.mkdir(exist_ok= True)

    for file_name in files[extension]:
        filepath = os.path.join(cwd, file_name)
        try:
            shutil.copy(filepath, os.path.join(cwd, extension)) # Just copy things over for now
        except FileExistsError:
            # Match with numbers between 1- inf amount of times
            fmatch = re.search("\d+",FileExistsError.filename)
            fn = file_name + '1' if ('0' < fchar < '9') else fchar
                

            continue
