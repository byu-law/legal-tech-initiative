# rename.py
# Used to rename a group of specified files (glob) from one path to another
from pathlib import Path
import shutil
import typing
import os

SOURCE_PATH: typing.Final = ""  # 'Constant' used to specify the relative path where the files can be found
TARGET_PATH: typing.Final = ""  # 'Constant' used to specify the relative path where to place the new, renamed files (don't forget the trailing /)
FILE_TYPE_GLOB: typing.Final = ""  # 'Constant' used to define the file search parameters (glob)

# Create the folder location for the target path
os.makedirs(os.path.dirname(p=TARGET_PATH), exist_ok=True)

# Iterate through all the files found in the source path (rglob == recursive glob)
for file in Path(SOURCE_PATH).rglob(pattern=FILE_TYPE_GLOB):
    folder_name: str = os.path.basename(p=file.parent)  # Get the name of the folder the file was found in and store it
    file_name: str = os.path.basename(p=file)  # Get the name of the file and store it
    new_name: str = os.path.join(TARGET_PATH, f"{folder_name}-{file_name}")  # Store the 'new' name of the file (using the target path)

    # DEBUG
    # print(f"Located file '{file_name}' found in folder '{folder_name}'")
    # print(f"Saving to {new_name}\n")

    # Copy the located file to the new location
    # shutil.copy(src=file, dst=new_name)
