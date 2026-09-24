# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def counting_vowels_and_consonants(string):
    vowel_count = 0
    consonant_count = 0
    for character in string:
        if character.isalpha():
            if character == "a" or character == "A" or character == "e" or character == "E" or character == "i" or character == "I" or character == "o" or character == "O" or character == "u" or character == "U":
                vowel_count += 1
            else:
                consonant_count += 1
    return (vowel_count, consonant_count)

def average_vowels_and_consonants(paragraph):
    sentence_count = 0
    current_sentence = ""
    total_vowels = 0
    total_consonants = 0

    for character in paragraph:
        if character == "." or character == "!":
            sentence_count += 1
            current_vowels, current_consonants = counting_vowels_and_consonants(current_sentence)

            total_vowels += current_vowels
            total_consonants += current_consonants
            current_sentence = ""
        else:
            current_sentence += character

    average_vowels = total_vowels / sentence_count
    average_consonants = total_consonants / sentence_count

    return (sentence_count, average_vowels, average_consonants)

richard_feynman_analysis = average_vowels_and_consonants(paragraph)

print (f"The average number of vowels per sentence in Richard Feynman's quote is {richard_feynman_analysis[1]}.")
print (f"The average number of consonants per sentence in Richard Feynman's quote is {richard_feynman_analysis[2]}.")