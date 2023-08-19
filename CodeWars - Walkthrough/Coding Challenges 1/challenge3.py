""""
Trolls are attacking your comment section!
A common way to deal with this is to remove all of the vowels in the troll's
comments, neutralizing the thread.

Your task is to write a function that takes a string, and return a new
string with all the vowels removed.
Example:
    "This website is for losers LOL!" would becom "Ths wbst s fr lsrs LL!".
    Note: y is not considered a vowel.
 - 7kyu Hardness
"""


# My Code
# def disemvowel(comment):
#     comment = comment.replace("a","")
#     comment = comment.replace("e","")
#     comment = comment.replace("i","")
#     comment = comment.replace("o","")
#     comment = comment.replace("u","")
#     comment = comment.replace("A","")
#     comment = comment.replace("E","")
#     comment = comment.replace("I","")
#     comment = comment.replace("O","")
#     comment = comment.replace("U","")
#     return comment

# def disemvowel(comment):
#     vowels = ['a','e','i','o','u']
#     for vowel in vowels:
#         comment = comment.replace(vowel, "")
#         comment = comment.replace(vowel.upper(), "")
#     return comment


# refactor
# def disemvowel(comment):
    # new_str = ""
    # for chars in comment:
    #     if chars.lower() not in 'aeiou':
    #         new_str += chars
    # return new_str
    # return "".join(chars for chars in comment if chars.lower() not in 'aeiou')
    # return "".join(chars if chars.lower() not in 'aeiou' else "" for chars in comment)



# Video Implementation / Alternate Implementations
# def disemvowel(comment):
#     vowels = 'aeiou'
#     for v in vowels:
#         comment = comment.replace(v, "")
#         comment = comment.replace(v.upper(), "")
#     return comment

# def disemvowel(comment):
    # return "".join(c for c in comment if c.lower() not in "aeiou")

def disemvowel(comment):
    return comment.translate(str.maketrans({i:None for i in 'aeiouAEIOU'}))
    # return comment.replace((i for i in 'aeiouAEIOU'), "")


# My Test
if __name__ == '__main__':
    print(disemvowel("This website is for losers LOL!"))
