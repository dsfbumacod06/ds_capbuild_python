""""
Hashtag Generator
    - Starts wutg a hashtag (#)
    - All words must have their first letter capitalized.
    - if the final result is longer than 140 characters, return falase.
    - if the input or result is an empty string, it must return false.
Example:
    "   Hello there thanks for trying my Kata"  # -> '#HelloThereThanksForTryingMyKata'
    "    Hello    World    " # -> '#HelloWorld'
    "" # -> False
 - 5kyu Hardness
"""



# My Code
# def generate_hastag(s):
#     hash_str = "#" + s.title().replace(" ", "") if not len(s) == 0 else False
#     hash_str = False if len(str(hash_str)) > 140 else hash_str
#     return hash_str


#Refactor

# Video Implementation / Alternate Implementations
# def generate_hastag(s):
#     result = "#" + s.title().replace(" ", "")
#     if result == "#" or len(result) > 140:
#         return False
#     return result 

def generate_hastag(s):
    result = "#" + s.title().replace(" ", "")
    return result if result != "#" and len(result) < 140 else False




# My Test
if __name__ == '__main__':
    print(generate_hastag("   Hello there thanks for trying my Kata"))
    print(generate_hastag(""))
    print(generate_hastag("   Hello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my KataHello there thanks for trying my Kata"))
