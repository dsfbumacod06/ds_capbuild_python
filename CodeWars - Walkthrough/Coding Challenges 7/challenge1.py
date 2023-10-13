'''
First Variation on Caesar Cipher

     The action of a Caesar cipher is to replace each plaintex letter (a-z|A-Z) with a different one a fixed number of places up or down the alphabet.
     
     This program performs a variation of the Caesar shift. The shift incfreases by 1 for each character on each iteration.
     
     If the shift is initially 1, the first character of the message will be shifter by 1, the second character will be shifted by 2, etc.
     
     Coding: Parameters and return of the function moving shift:
        param s: string to be coded
        param shift: an integer giving the initial shift
        
    The function "movingShift" first codes the entire string and then returns an array of strings containing the coded string in 5 parts. (Five parts to avoid more risks, the coded message will be given to five runners, one piece for each runner)
    
    If possible, the message will be equally divided by message length between five runners. If it is not possible, parts 1 to 5 will have subsequently non-increasing lengths such that parts 1 to 4 are at least as long as when evenly divided, but at most 1 longer. If the last part is the emplty string, this empty string must be shown in the resulting array.
    
    For example, if the coded message has a length of 17, the five parts will have lengths of 4, 4, 4, 4, 1. The parts 1,2,3,4 are evenly split, and the last part of length 1  is shorter. If the length is 16, the parts will be of lengths 4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay at home since his part is the empty string. If the length is 11, equal parts woul be of length 2.2, hence the parts will be of lengths 3, 3, 3, 2, 0.
    
    You will also implement av demovingShift:
        param s: an array of strings ( list of 5 strings, output of movingshift)
        param shift: the integere shift
        
    demovingShift returns a string
    
    Examples:
    u = "I should have known that you would have a perfect answer for me!!!"
    movingShift(u, 1) returns: 
    v = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
    lengths: 14, 14, 14, 14, 10
    demovingShift(v, 1) returns:
    "I should have known that you would have a paerfect answer for me!!!"
'''

# mycode
# def movingShift(s, shift):
#     lst = list(enumerate(s,shift))
#     str_lst = []
#     elem_len = len(s)//5 + 1
#     while len(lst) > 0:
#         if len(lst) > elem_len:
#             str_lst.append(lst[:elem_len])
#             lst = lst[elem_len:]
#         else: 
#             str_lst.append(lst)
#             lst = ""
#     while len(str_lst) < 5:
#         str_lst.append("")
    
#     words = []
#     for item in str_lst:
#         words.append("".join([letter_Shifter(letter[1], letter[0]) for letter in item]))
#     return words

        
# def letter_Shifter(letter, shift):
#     if not letter.isalpha(): return letter
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     upper = "ABCDEFHIJKLMNOPQRSTUVWXYZ"
#     lst_lower = list(enumerate(lower))
#     lst_upper = list(enumerate(upper))
#     dct_lower = {key: value for key, value in lst_lower}
#     dct_upper = {key: value for key, value in lst_upper}
    
    
#     if letter in lower:
#         ind_shift = lower.index(letter) + shift
#         while ind_shift > 25:
#             ind_shift -= 26
#         return dct_lower[ind_shift]
#     else:
#         ind_shift = upper.index(letter) + shift
#         while ind_shift > 25:
#             ind_shift -= 26
#         return dct_upper[ind_shift]
    
    
# def demovingShift(s, shift):
#     s = enumerate("".join(s), shift)
#     new_word = []
#     for letter in s:
#         new_word.append(letter_deShifter(letter[1], letter[0]))
#     return "".join(new_word)

# def letter_deShifter(letter, shift):
#     if not letter.isalpha(): return letter
#     lower = "abcdefghijklmnopqrstuvwxyz"
#     upper = "ABCDEFHIJKLMNOPQRSTUVWXYZ"
#     lst_lower = list(enumerate(lower))
#     lst_upper = list(enumerate(upper))
#     dct_lower = {key: value for key, value in lst_lower}
#     dct_upper = {key: value for key, value in lst_upper}
    
    
#     if letter in lower:
#         ind_shift = lower.index(letter) - shift
#         while ind_shift < 0:
#             ind_shift += 26
#         return dct_lower[ind_shift]
#     else:
#         ind_shift = upper.index(letter) - shift
#         while ind_shift < 0:
#             ind_shift += 26
#         return dct_upper[ind_shift]
    
    
# video code
import string

alphabet = string.ascii_lowercase

def movingShift(s, shift):
    is_uppercase = [c.isupper() for c in s]
    s = s.lower()
    letters = []
    result = "".join([alphabet[(alphabet.index(c) + i) % len(alphabet)] if c in alphabet else c for i, c in enumerate(s, shift)])
    # for i, c in enumerate(s, shift):
    #     if c in alphabet:
    #         letters.append(alphabet[(alphabet.index(c) + i) % len(alphabet)])
    #     else: 
    #         letters.append(c)
    # result = "".join([c.upper() if is_uppercase[i] else c for i, c in enumerate(letters)])
    
    result = "".join(c.upper() if is_uppercase[i] else c for i, c in enumerate(result))
    if len(result) % 5 == 0:
        part_length = len(result) // 5
        return [result[i * part_length:(i + 1) * part_length] for i in range(5)]
    else:
        part_length = len(result) // 5 + 1
        return [result[i * part_length: (i+1) * part_length] for i in range(4)] + [result[4*part_length:]]  # if the slice gets larger than the length of the stringm it still retains the value of the end of the string and does not add empty spaces. smheart! slices with both arguments larger than the length of the string returns null or empty string!! perfect!!!
    # return result
    
def demovingShift(s, shift):
    s = "".join(s)
    is_uppercase = [c.isupper() for c in s]
    s = s.lower()
    result = "".join([alphabet[(alphabet.index(c) - i) % len(alphabet)] if c in alphabet else c for i, c in enumerate(s, shift)])
    result = "".join(c.upper() if is_uppercase[i] else c for i, c in enumerate(result))
    return result


def main():
    # print(alphabet)
    text = "I should have known that you would have a perfect answer for me!!!"
    x = movingShift(text, 1) # ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
    print(x)
    # v = demovingShift(x, 1)  # I should have known that you would have a perfect answer for me!!!
    # print(v)
    print((movingShift("Some text11", 1)))
    # letter_Shifter("!!!")
    # print(letter_Shifter("x", 1)) # y
    # print(letter_Shifter("z", 1)) # a
    # print(letter_Shifter("Q", 4)) # U
    # print(letter_Shifter("p", 1)) # q
    # print(letter_Shifter("b", 29)) # e
    # print(letter_deShifter("x", 1)) # w
    # print(letter_deShifter("z", 1)) # y
    # print(letter_deShifter("Q", 4)) # M
    # print(letter_deShifter("p", 1)) # o
    # print(letter_deShifter("b", 29)) # y
    # pass

if __name__ == "__main__":
    main()