""""
Write a function that takes in a string of one or more words, and returns the
same string but with all five or more words revers like the name of this kata (Stop nginnipS My sdroW).
    - Strings passed will consist of only letters and spaces.
    - Spaces will be included only when more than one word is present.
Example:
    spinWords("Hey my fellow warriors") -> "Hey wollef sroirraw"
    spinWords("This is a test") -> "This is a test"
    spinWords("This is another test") -> This is rehtona test"
 - 6kyu Hardness
"""


# My Code
# def spinWords(sentence):
#     words = sentence.split(" ")
#     i = 0
#     for w in words:
#         if len(w) >= 5:
#             words[i] = w[::-1]
#         i += 1
#     return " ".join(words)

#refactor
# def spinWords(sentence):
#     words = sentence.split(" ")
#     # words = [word[::-1] if len(word) >= 5 else word for word in words]
#     words = [word if len(word) < 5 else word[::-1] for word in words]
#     return " ".join(words)

# Video Implementation / Alternate Implementations
# def spinWords(sentence):
    # words = sentence.split(" ")
    # words = [word[::-1] if len(word) >= 5 else word for word in words]
    # return " ".join(words)
    # return " ".join([word[::-1] if len(word) >= 5 else word for word in words])
    

def spinWords(sentence):
    return " ".join([word[::-1] if len(word) >= 5 else word for word in sentence.split()])



# My Test
if __name__ == '__main__':
    print(spinWords("Hey my fellow warriors"))
    print(spinWords("This is a test"))
    print(spinWords("This is another test"))