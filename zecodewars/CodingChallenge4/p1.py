'''
Like system of facebook pages
[] -> no one likes this
["Peter"] -> Peter likes this
["Jacob", "Alex"] -> Jacob and alex likes this
["Max", "John", "Mark"] -> Max, John, and Mark likes this.
["Alex", "Mark", "Jacob", "Max"] -> Alex, Mark, and 2 others likes this.
'''

def view_likes(names):
    n = len(names)
    return {
        0: "No one likes this",
        1: "{} likes this.",
        2: "{} and {} like this.",
        3: "{}, {}, and {} like this",
        4: "{}, {}, and {num} others like this."
    }[min(4,n)].format(*names[:3],num=(n-2))



print(view_likes([]))  # case 1
print(view_likes(["Peter"]))  # case 2
print(view_likes(["Jacob", "Alex"]))  # case 3
print(view_likes(["Max", "John", "Mark"]))  # case 4
print(view_likes(["Alex", "Mark", "Jacob", "Max"]))  # case 5

ages = [5,4,3,2,1]

def add_three_numbers(a, b, c):
    return a + b + c

print(add_three_numbers(*ages[:3]))