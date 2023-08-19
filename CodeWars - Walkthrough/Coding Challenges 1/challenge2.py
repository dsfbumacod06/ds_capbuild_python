""""
Complete the solution so that it returns true if the first argument (string), 
ends with the 2nd argument (string).
Example:
    solution('abc', 'bc') - returns true
    solution('abc', 'd') - returns false
 - 7kyu Hardness
"""


# My Code
# def solution(starting,ending):
#     end_len = len(ending)
#     if starting[-end_len:] == ending:
#         return True
#     else:
#         return False


# Video Implementation / Alternate Implementations
def solution(starting,ending):
    return starting.endswith(ending)




# My Test
if __name__ == '__main__':
    # solution = str.endswith # also works
    print(solution("abc","bc"))
    print(solution("abc","d"))