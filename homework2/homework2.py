# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a version control tool that records your changes and it runs on your computer. GitHub is an online service 
# where you can save your Git projects and collaborate with others. GitBash is the Windows terminal that lets you run 
# Git commands.

# 2) What’s the difference between the terminal and the command line?
# The terminal is the application you open to type text commands. The command line is the text-based way of interacting
# with a computer by typing commands, rather than clicking buttons.

# 3) How does Windows PowerShell differ from Git Bash?
# PowerShell is Windows' general command shell for all purposes, but Git Bash is a shell installed specifically with git
# for Windows. Both can run Git commands when installed.

# 4) What’s the difference between Anaconda, conda, and Python?
# Python is the programming language. However, conda is a tool for installing packages and managing separate project
# environments. Anaconda is a larger Python distribution that includes Python, conda, and many other data-science
# related tools and packages.

# 5) What is VS Code? 
# VS Code is a free, open-source code editor that can be used to write/organize/run/debug code and is made by Microsoft.

# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# A Jupyter Notebook is a document where you can write and run code in small cells and see the output right underneath.
# It is more simple and focused on one notebook document. A Jupyter Lab is a fuller workspace for notebooks and other
# files, and can display multiple at a time.

# 7) What does ~/ mean?
# ~/ means your home folder, which is your personal top-level directory in the temrinal.

# 8) What’s the difference between an absolute path and a relative path?
# An absolute path gives you the full location of a file, whereas the relative path gives its location starting from the 
# folder you are currently in.

# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# absolute: /Users/anropaul/Desktop/python_decal_fa26/course_assignments/homework2
# relative: ../course_assignments/homework2

# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..

# 11) What would rm ./ do in your current directory? (Don’t try it!)
# rm ./ removes the current directory

# 12) What do the following commands do?
# git add: selects changes to include in your next saved version.
# git commit: saves the saved changes as a checkpoint in your local Git repository.
# git push: uploads your current commits to a remote repository (like GitHub)

# 13) What's the difference between "git add ." and "git add <file>"?
# "git add ." stages all changes in your current folder and all the sub folders. "git add <file>" stages only the file
# whos name is written.

# 14) What do "git status" and "git log -1" do?
# "git status" shows what has changed in your repo like any modified/staged/untracked files and whether your branch is
# ahead/behind GitHub. "git log -1" shows details for only the most recent commit.

# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning is done only once at the beginning, to download a full repository from GitHub onto your computer, including
# any files or commit history. Pulling is used after you have already cloned your repository to download and merge newer
# changes from GitHub into your existing local copy (that you made through cloning).

# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# I think my most frustrating error was not being able to save my nano files. I think it is because ^S is not a command on
# my end, and I just wasn't reading the small text correctly when it asked me further questions about saving under
# the same file name too. I troubleshooted it by zooming in and really reading everything carefully step-by-step, rather
# than just blindly following the instructions.

# 17) What’s a question you still have? What’s something you’re confused about?
# I'm still a little confused about how Git and GitHub interact, and how changes update on the browser end, where files save,
# etc. I have a more theortical understanding that Git is the local interface and GitHub saves it online, but I think with more
# experience I will get a better intuitive understanding for how it all works.

# 18) Tell me a fun fact!
# I have a black belt in Taekwondo!

# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)

print (75 // 10 % 10) # Divides 75 by 10 (rounding down to an integer) and then returns the remainder of dividing that by 10.
# Effectively extracts the first digit of 75.
