""""
Write a function that will return the count of distinct case-insensitive alphabetic 
characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets(both uppercase, and lowercase)
and numeric digits.
Example:
    'abcde' -> 0
    'aabbcde' -> 2
    'aabBcde' -> 2
 - 6kyu Hardness
"""


# My Code
def duplicate_count(text):
    text = text.lower()
    counter = 0
    for char in text:
        # if len(text) -1 > len(text.translate(str.maketrans({char:None}))):
        if len(text) -1 > len(text.replace(char,"")):
            counter += 1
            text = text.replace(char,"")
    return counter

#refactor


# Video Implementation / Alternate Implementations
# def duplicate_count(text):
#     occurred = []
#     found = []
#     counter = 0
#     for letter in text:
#         if letter.lower() not in occurred:
#             occurred.append(letter.lower())
#         else:
#             if letter.lower() not in found:
#                 counter += 1
#                 found.append(letter.lower())
#     return counter

# def duplicate_count(text):
#     return [c for c in set(text.lower()) if text.lower().count(c)>1]
    # return len([c for c in set(text.lower()) if text.lower().count(c)>1])
    




# My Test
if __name__ == '__main__':
    print(duplicate_count("abcde")) # 0
    print(duplicate_count("aabBcde")) # 2
    print(duplicate_count("aa11bcde212")) # 3
    print(duplicate_count("Indivisibility")) # 1
    print(duplicate_count("Indivisibilities")) # 2