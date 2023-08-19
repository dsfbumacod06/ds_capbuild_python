""""
Where my anagrams at?
Two words are anagrams of each other if they both contain the sam letters.
'abba' 'baab' -> true
'abba' 'abbba' -> false

Write a function that will find all anagrams of a word from a list.
You will be given two inputs, a word and an array with words. You should
return an array of alll the anagrams or an empty array if there are none.
Example:
    
 - 5kyu Hardness
"""



# My Code
def anagrams(word, words):
    return [entry for entry in words if sorted(word) == sorted(entry)]



#Refactor


# Video Implementation / Alternate Implementations

# My Test
if __name__ == '__main__':
    print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))