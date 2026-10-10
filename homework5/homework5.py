# -- 2) Homework 1 + 2 Review --

# 2.1 Vocabulary Review

# 1. Git vs GitHub: Git is a local version control software that tracks changes in your code, while GitHub is on a cloud and stores 
# repositories online

# 2. Terminal vs Command Line: A command line is an interface where you can type text commands while a terminal is the window that 
# runs the commands

# 3. Local vs Remote Repository: A local repository is stored directly on your laptop, but a remote repository is on another server 
# (just like GitHub)

# 4. Version Control: A system that records the changes you make to files, so you have access to different versions

# 5. Staging Area: A middle area in Git where files are prepared before you save them to a repository

# 6. git add: Adds file changes from a working area to a staging area, to prepare them for being commit.

# 7. git commit: Takes a "snapshot" of the working area, and saves changes to the local repository history (and you add a message using "-m")

# 8. git push: Uploads local repository to a remote repository.

# 9. git status: Reports the status of the working directory and staging area, showing what files have been modified.

# 10. git pull: Fetches and integrates changes from a remote repository onto your local branch.

# 11. pwd: Stands for "present working directory" and prints the absolute path (from the root) of the directory you are currently in.

# 12. ls: Lists all the files and subdirectories located inside the current working directory.

# 13. cd: Stands for "change directory" and navigates you between folders.

# 14. nano: Opens a terminal editor used to create/edit text files directly from the command line.

# 15. touch: Creates/opens a file (creates if it doesn't yet exist, or just modifies it)

# 16. mv: Moves/renames files and directories.

# 17. rm: Deletes files or directories from the system.

# 18. cat: Combines and displays the contexts of a text file in the terminal output.

# 2.2 A Directory Tree

# 1. pwd

# 2. ls

# 3. cd ..
# cd brianna_repo
# git pull

# 4. mv homework.py ../judy_decal/homework

# 5. cd ../judy_decal/homework

# 6. cat homework.py

# 7. git add .
# git commit -m "finished hw!" 
# git push origin main

# 8. The error occurs because the remote repository contains changes that do not exist in the local working directory. You have to pull
# those changes first before overwriting them.
# git pull origin main 
# git push origin main

# 9. cd ~/Recent/

# -- 3) Homework 3 Review --

# 3.1 Data Types

def checkDataType(input): # returns a string indicating the input's data type 
    input_classes = {
        int: "integer",
        float: "float",
        bool: "boolean",
        str: "string",
        list: "list",
        dict: "dictionary",
        tuple: "tuple"
    }

    return input_classes[type(input)]

# 3.2 Conditionals

def evenOrOdd(integer): # takes an integer and returns whether it is even or odd
    if integer % 2 == 0:
        return 'Even'
    return 'Odd'

# -- 4) Loops --

def sumWithLoop (list_of_ints): # returns sum of elements in a list of integers
    sum = 0
    for int in list_of_ints:
        sum += int
    return sum

# -- 5) Homework 4 Review --

# 5.1 Lists

def duplicateList(list): # given a list, returns a list with each element duplicated
    new_list = []
    for element in list:
        new_list += [element, element]
    return new_list

print(duplicateList([1, 2, 3, 4, 5]))

# 5.2 Debugging

def square(num): # missing colon in original version
    return num * num