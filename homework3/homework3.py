# homework3.py

# --- 3) Print Functions ---

# 3.1
def say_goodbye(name):
    # prints a goodbye message to the inputted name
    print("Goodbye,", name)

# 3.2
def print_area(radius):
    # prints the radius of a circle with the inputter radius
    print("The area of the circle is", 3.14 * radius ** 2)

# --- 4) Return Functions ---

# 4.1
def subtract(a, b):
    # returns the difference of a and b
    return a - b

def multiply(a, b):
    # returns the product of a and b
    return a * b

def divide(a, b):
    # returns the quotient of a and b
    return a / b

# --- 5) Conditionals ---

# 5.1
def what_to_wear(temps):
    # returns a tuple with minimum and maximum values of list of temperatures
    return (min(temps), max(temps))

# 5.2
def is_weekend(day):
    # takes an integer (Mon = 1, Tues = 2, ... Sun = 7) and returns True if its the weekend
    if day > 5:
        return True
    else:
        return False

# 5.3
def fuel_efficiency(distance, fuel):
    # returns fuel efficiency in miles per gallon
    return distance/fuel

# 5.4
def encrypt(data):
    # returns an encrypted version of the inputted data, where the last digit is moved to the front of the number
    last_digit = str(data % 10)
    rest = str(data // 10)
    return int(last_digit + rest)

# --- 6) Loops ---

# 6.1
def power(x, y):
    # returns x raised to the power of y
    total = x
    for i  in range(y-1):
        total *= x
    return total

# 6.2.1 #1
def for_loop_min(integers_list):
    # uses a for loop to return the minimum value of an inputted list of integers
    min = integers_list[0]
    for int in integers_list:
        if int < min:
            min = int
    return min

# 6.2.1 #2
def for_loop_max(integers_list):
    # uses a for loop to return the maximum value of an inputted list of integers
    max = integers_list[0]
    for int in integers_list:
        if int > max:
            max = int
    return max

# 6.2.2 #1
def while_loop_min(integers_list):
    # uses a while loop to return the minimum value of an inputted list of integers
    index = 0
    min = integers_list[index]
    while index < len(integers_list):
        if integers_list[index] < min:
            min = integers_list[index]
        index += 1
    return min

# 6.2.2 #2
def while_loop_max(integers_list):
    # uses a while loop to return the maximum value of an inputted list of integers
    index = 0
    max = integers_list[index]
    while index < len(integers_list):
        if integers_list[index] > max:
            max = integers_list[index]
        index += 1
    return max

# 6.3
def sum(integer):
    # returns the fum of the digits of an inputted integer
    sum = 0
    while integer > 0:
        sum += integer % 10
        integer = integer // 10
    return sum

# --- 7) Running Your Script ---

integers_list = [1, 2, 3, 100000, -3, 5, 8]
result = while_loop_min(integers_list)

print (f"The result of the function that uses a while loop to return the minimum value in a list (6.2.2 #1) with the list {integers_list} is {result}.")