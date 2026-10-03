#homework4.py

# -- 3 Lists --

# 3.1 List Operations

favorite_foods = ["pizza", "lasagna", "chicken", "noodles"]

#1: prints second item of list
print(favorite_foods[1]) 

#2: prints last food (using negative indexing)
print(favorite_foods[-1]) 

#3: adds new item at end of list
favorite_foods.append("sandwich") 

#4: inserts "apple" to beginning of list
favorite_foods.insert(0, "apple") 

#5: removes third item of list
favorite_foods.remove("lasagna") 
# I encountered this error:
# ValueError: list.remove(x): x not in list
# I initially had written favorite_foods.remove(2).
# I accidentally put the index of the word I wanted to remove rather than the word. 
# I fixed it by putting the string in the paranthesis.

#6: prints length of list
print(len(favorite_foods)) 

#7: prints each food in uppercase
for food in favorite_foods:
    print(food.upper())

#8: creates new list with first and last item
new_list = favorite_foods[0:1] + favorite_foods[-1:]

#9: checks if "potato" is in the list
if "potato" in favorite_foods:
    print ("A potato!")
else:
    print ("No potato!")

# 3.2 List Operations

numbers = []
for number in range(0, 21):
    numbers += [number]
# I encountered this error:
# TypeError: 'int' object is not iterable
# I initially had written numbers += number
# I forgot that the "number" variable is an integer, which you can't add to a list.
# I fixed it by putting square brackets around the variable "number."

#1: returns the first 15 elements
def get_first_15(numbers):
    return numbers[0:15]

output1 = get_first_15(numbers)

# I encountered this error:
# TypeError: 'function' object is not subscriptable
# I initially had written get_first_15[0:15]
# I accidentally called the function name when slicing, rather than the inputted list.
# I fixed it by changing the name of the list to "numbers" (the input).

#2: returns every 5th element
def get_every_5th(list):
    return list[0::5]

output2 = get_every_5th(output1)

#3: returns every 3rd element of reversed list
def reverse_and_stride(list):
    reverse_list = list[::-1]
    return reverse_list[::3]

output3 = reverse_and_stride(output2)
print(output3)

# 3.3 Nested Lists

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 3.1.1 Nested List Operators

#1: prints third row
print(numbers[2])

#2: prints second item in second row
print(numbers[1][1])

#3: adds [10, 11, 12] as new row
numbers.append([10, 11, 12])

#4: functions loops through each row, sums all numbers, and returns total
def sum_nested(numbers):
    sum = 0
    for row in numbers:
        for column in row:
            sum += column
    return sum

# 3.4 Create a 5x5 List

def five_by_five():
    five_by_five_list = []
    current_num = 1

    for row in range (0,5):
        row_list = []
        for number in range(1,6):
            row_list.append(current_num)
            current_num += 1
        five_by_five_list.append(row_list)
    return five_by_five_list



five_by_five_list = five_by_five()

#1: function that replaces multiples of 3 with "?"

def multiples_of_three(list):
    for each_list in list:
        for index in range(len(each_list)):
            if each_list[index] % 3 == 0:
                each_list[index] = "?"
    return list

updated_list = multiples_of_three(five_by_five_list)

#2: function that sums all elements not "?"

def sum_numbers(list):
    sum = 0
    for each_list in list:
        for index in range(0, len(each_list)):
            if each_list[index] != "?":
                sum += each_list[index]
    return sum

updated_list2 = sum_numbers(updated_list)

# -- Dictionaries --

# 4.1 Dictionary Operations

ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}

#1: prints Katie's age
print (ages["Katie"])

#2: changes Mira's age to 100
ages["Mira"] = 100

#3: adds "Milana" with an age of 52
ages["Milana"] = 52

#4: removes "Milana" from dictionary
del ages["Milana"]

#5: prints out each person's name/age

for name, age in ages.items():
    print(f"{name}, {age}")

