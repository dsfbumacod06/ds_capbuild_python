# Remove exclamation points. - 8kyu Hardness
# My Code
# x = input("Please enter a string: ")
# x = x.replace("!", "")
# print(f'Qualified String: {x}')

# Video Implementation
def remove_exclamation_marks(s):
    return s.replace("!", "")


# My Test
if __name__ == '__main__':
    msg = remove_exclamation_marks("Hello!! W!orld!!")
    print(msg)