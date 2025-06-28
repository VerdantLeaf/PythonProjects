from pathlib import Path
import os
import shutil


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
        
        if len(ext) == 1 and not file_name.startswith('.'): # Just don't handle a LICENSE file at this moment
            continue

        ext = ext[-1]

        extensions.append(ext)
        
        try:
            print(file_name)
            files[ext].append(file_name)
        except KeyError:
            files.update({ext: [file_name]})


print(files)

# # make the new directories
for extension in extensions:
    dir = Path(extension)
    dir.mkdir(exist_ok= True)

    for file_name in files[extension]:
        filepath = os.path.join(cwd, file_name)
        shutil.copy(filepath, os.path.join(cwd, extension)) # Just copy things over for now