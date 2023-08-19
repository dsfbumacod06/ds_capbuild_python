""""
Write a function that, given a string of text (possibly with punctuation and line breaks),
returns an array of the top-3 most occuring words in descending order of the number of occurences.

Assumptions.
    A word is a string of letters from (A to Z), optionally containing one or more apostrophes in ASCII.
    Matches should be case-insensitive
    Ties may be broken arbitrarily
    If a text containes fewer than three unique words, then either the top 2 or top 1 words should be returned.
    Empty if no words.

Example:
    top_3_words('In a something something something
    yes a a a banana kineso . . )
    ["a", "of", "on"]
 - 7kyu Hardness
"""

import collections

# My Code
def top_three_words(stringsets):
    words = []
    [words.extend(chunk.split()) for chunk in stringsets.lower().split(",")]
    top_3 = [i[0] for i in collections.Counter(words).most_common()[:3]]
    return top_3



#Refactor

# Video Implementation / Alternate Implementations


# My Test
if __name__ == '__main__':
    print(top_three_words("Anna banana, i love u a bunch, anna, anna, banana, banana, anna u"))
