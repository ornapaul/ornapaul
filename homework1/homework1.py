
#homework1.py

# --- 3.1 Variables and Data Types ---

a = 10
print (a)
print (type(a)) # a is an integer, a whole number with no decimals

b = 1.5
print (b)
print (type(b)) # b is a floating-point number, a real number that contains a decimal point

c = 3j
print (3j)
print (type(3j)) # c is a complex number, with a real and imaginary part

d = "hello"
print (d)
print (type(d)) # d is a string, an ordered sequence of characters stored between quotation marks

e = [1, 2, 3]
print (e)
print (type(e)) # e is a list, a sequence data type stored between square brackets

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print (type(f)) # f is a dictionary, a mapping type that stores data in key-value pairs

g = (1, 2)
print (g)
print (type(g)) # g  is a tuple, a collection that stores multiple items in a single variable

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h)) # h is a list, a sequence data type stored between square brackets

i = True
print (i)
print (type(i)) # i is a boolean, which is a data type that has only two possible values, True and False

j = None
print (j)
print (type(j)) # j is a special constant NoneType used to represent the absence of a value

k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list, a sequence data type stored between square brackets

l = str(14)
print (l)
print (type(l)) # l is a string, an ordered sequence of characters stored between quotation marks

m = 1e4
print (m)
print (type(m)) # m is a floating-point number, a real number that contains a decimal point

# 1) I found 9 different data types.
# 2) The data types are integer, floating-point number, complex number, string, list, dictionary, tuple, boolean, and NoneType.
# 3) The variables with the same data type are b & m, d & l, e & h & k
# 4) l was a string. It is not an integer because it was inside the str() function, which converts objects into strings.
# 5) One more data type is range.

n = range (6)
print (n)
print (type(n)) # n is a range, which represents a sequence of numbers

# --- 3.2 Booleans ---

print (10 > 9) # True, 10 is greater than 9
print (10 == 9) # False, 10 does not equal 9
print (10 <= 9) # False, 10 is greater than 9
print (bool("abc")) # True, a nonempty string is a truthy value
print (bool(123)) # True, a nonzero number is a truthy value
print (bool(["apple", "cherry", "banana"])) # True, a nonempty list is a truthy value
print (bool(True)) # True, True is a truthy value
print (bool(False)) # False, False is a falsy value
print (bool(0)) # False, 0 is a falsy value
print (bool("")) # False, an empty string is a falsy value
print (bool(" ")) # True, a nonempty string is a truthy value
print (bool()) # False, an empty tuple is a falsy value
print (bool([])) # False, an empty list is a falsy value
print (bool({})) # False, an empty dictionary is a falsy value
print (bool(True and False)) # False, "and" requires both to be True to be True. Since one of them is False, the whole expression is False
print (bool(True and True)) # True, since both are True, the whole expression is True
print (bool(False and False)) # False, since both are False, the whole expression is False
print (bool(True or False)) # True, "or" requires at least one value to be True. Since one of the values is True, the whole expression is True.
print (bool(True or True)) # True, since at least one value is True, the whole expression is True
print (bool(False or False)) # False, since neither value is True, the whole expression is False
print (bool(not(False))) # True, "not" simply provides the opposite value of the boolean. The opposite of False is True.
print (bool(not(True))) # False, the opposite of True is False.

# 1) Expressions return true when their relationship stated is correct, and false when it is not. When "or" is applied, at least one needs to be True to make the result True. When "and" is applied, both need to be True.
# 2) I was surprised by bool (" "), because I wasn't sure whether the space would make it count as a nonempty string, but it returned True.
# 3) 1 == 1 will return True becaues 1 does equal 1.
# 4) bool (False and True) will return False, because at least one of the values is False.

# --- 3.3 Operators ---

# 3.3.1 Arithmetic Operators

print (10 + 5) # 15, + performs addition
print (10 - 5) # 5, - performs subtraction
print (2 * 4) # 8, * performs multiplucation
print (6 / 3) # 2.0, / performs division
print (5 % 2) # 1, % gives the remainder of dividing
print (3 ** 2) # 9, ** raises to the power
print (15 // 2) # 7 , // performs floor division (divides and rounds down so there's no decimal)

# 3.3.2 Comparison Operators

print (5 == 2) # False, == checks if the two values are equal
print (10 != 10) # False, != checks if the two values are not equal
print (2 < 5) # True, < checks if the first value is less than the second
print (12 > 5) # True, > checks if the first value is greater than the second
print (5 <= 6) # True, <= checks if the first value is less than or equal to the second
print (1 >= 10) # False, >= checks if the first value is greater than or equal to the second

# 3.3.3 Assignments Operators

x = 5
x += 5
x -= 4
x *= 3

# 3.3.4 Logical Operators

# 1) The operator "and" results in True if both values are True, and False if otherwise.
# True expression --> 3 == 3 and 4 == 4
# False expression --> 3 == 3 and 4 == 5

# 2) The operator "or" results in True if at least one of the values is True, and False if both are False.
# True expression --> 3 == 3 or 4 == 5
# False expression --> 3 == 4 or 4 == 5

# 3) The operator "not" results in True if the expression is False, and False if the expression is True.
# True expression --> not (3 == 4)
# False expression --> not (3 == 3)

# More Questions

# 1) / is regular division, that results in the exact number with a decimal point. // is floor division and rounds down to the nearest whole integer after dividing.
# 2) % returns just the remainder of dividing, whereas // rounds down (as to return the quotient with no remainder)
# 3) I would use % to calculate the remainder when dividing two numbers. If I wanted to find the remainder of diving 10 by 3 I would use 10 % 3 which would result in 1.
# 4) Assignment operators work by modifying the value of a variable. += adds the value to the right to the variable, -= subtracts the value, *= multiplies the value, and so on.

# --- 3.4 Strings ---

my_string = "hello"
print (my_string) # Prints: hello
print (my_string[0]) # Prints: h
print (my_string[1]) # Prints: e
print (my_string[2]) # Prints: l
print (my_string[3]) # Prints: l
print (my_string[4]) # Prints: o
print (my_string[-1]) # Prints: o
print (my_string[1:3]) # Prints: el
print (my_string[0:5:2]) # Prints: hlo
print (len(my_string)) # Prints: 5
print (my_string + "goodbye") # Prints: hellogoodbye
print (7 * my_string) # Prints: hellohellohellohellohellohellohello

# 1) Slicing means extracting a smaller part from a larger text string. I sliced my string for print (my_string[1:3]) and print (my_string[0:5:2]) 
# 2)
name = "Oski"
print ("Hello, my name is", name) # Prints: Hello, my name is Oski
# 3)
name = "Oski"
print(f"Hello, my name is {name}") # Prints: Hello, my name is Oski
# 4) The difference is that quesiton three uses an fstring, which makes it possible to embed any variable into the string using curly braces. 
# Number 2 instead separates the string and variables manually through quotation marks. The end result is the same.

# --- 3.5 Terminal Commands ---

# cd
# Changes directories. Use it to move from one folder to another
# Example: cd Desktop

# ls
# Displays contents of a directory. Use it to reveal the files and subfolders in a specific location.
# Example: ls

# ls -a
# Lists all files and directories in your current location, including hidden files.
# Example: ls -a

# mkdir
# Creates a new folder (directory).
# Example: homework_folder

# cat
# Displays the contents of a file directly in ther terminal. Use it to quickly read small text files.
# Example: cat notes.txt

# pwd
# Prints the full path of your present working directory. Use it to see where you are in the file system.
# Example: pwd

# cd ..
# Moves up one level to the parent folder of your current directory.
# Example: cd ..

# cd .
# Refers to the current directory, so the command keeps you in the same folder.
# Example: cd .

# cd ~
# Moves you to your home directory, the main personal folder for your user account.
# Example: cd ~

# cp
# Copes a file or folder from one location to another. It's used in the format cp source destination
# Example: cp notes.txt homework_folder/

# mv
# Moves a file or folder to a different location. It can also be used to rename a file or folder. It's used in the format mv source destination
# Example: mv notes.txt homework_folder/

# rm
# Deletes a file.
# Example: rm notes.txt

# clear
# Clears the visible text from the terminal screen. Use it to get a clean workspace.
# Example: clear

# grep
# Searches for a word, phrase or pattern inside a file, and prints the lines that contain a match. It's used in the format grep "searchterm" filename
# Example: grep "physics" notes.txt

# 1) 
# touch creates a new empty file if it does not already exist. If it is preexisting, touch updates the timestamp. Example: touch notes.txt
# head shows the first 10 lines of a file by default. Example: head notes.txt
# man opens the manual page for a command, explaining its purpose and available options. Example: man ls
 
# 2) ls and ls -a both list what all is in the current directory, but ls -a also shows hidden files and folders, whereas ls typically does not display those.

#3) A hidden file is one your computer does not show by default. It is usually to keep configuration and deeper system-related files from cluttering folders or accidentally being modified. 
# In macOS, dotfiles are typically hidden (files beggining with a .) Example: ls -l

#4)
# -l is used with ls to show a long, detailed list of files and folders. It includes information like permissions, owner, file size, and last-modified date.
# -r is used with rm to delete a folder and all files and folders inside it. Example: rm -r homework_folder
# -i is used with grep to search without caring about capitalization. Example: grep -i "physics" notes.txt
