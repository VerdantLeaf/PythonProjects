from pathlib import Path
import os
import shutil


subdirs = []    # Array of all the names of the current subdirectories
extensions = [] # Array to store all of the file extensions

cwd = Path.cwd()


for dir in cwd.iterdir():
    if dir.is_dir() and not dir.name.startswith('.'):
        subdirs.append(dir.name)

# Scan the current dir for all of the extensions
for file in os.listdir(cwd):
    filepath = os.path.join(cwd, file)
    # See if it is a file or a dir and that it doesn't start with .
    if os.path.isfile(filepath) and not file.startswith('.') :

        ext = file.split('.') # Split the string at the periods
        
        if len(ext) == 1 and "misc" not in extensions:
            extensions.append("misc")
        else:
            extensions.append(ext[len(ext) - 1])

# make the new directories
for extension in extensions: 
    dir = Path(extension)
    dir.mkdir(exist_ok= True)

# python ../PythonProjects/fileOranizer.py - nice 
# Transfer the files from the cwd to the subdirectories