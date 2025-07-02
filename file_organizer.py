"""

This script organizes files from a working directory into subdirectories based on the
file extensions of the files. 

I built this to refresh and substantialize my Python experience, as over the years it has
been a spotty, informal, and inconsistent education

Author: VerdantLeaf on GitHub

"""

from pathlib import Path
import os
import shutil
import re
from tabulate import tabulate

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
            # Search the file name for a number before the file extension
            match = re.search(r"(\d+)(?=\.[^.]+$|$)",FileExistsError.filename)
            if match:
                num = match.group(1) + 1
                fn = file_name + "-" + str(num)
            # if there is no number
            else:
                fn = file_name + "-1"

            filepath = os.path.join(cwd, fn)
            shutil.copy(filepath, os.path.join(cwd, extension))

# Change this to a function to allow repeated copy attempts that increment the number
# You can then change the number after getting a return indicating that it's failed
#def try_copy(cwd, file_name, extension):
