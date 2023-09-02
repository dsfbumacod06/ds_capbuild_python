'''
ROT13 Cipher
in: ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
out: NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm
'''


def rot13(message):
    instring = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    outstring = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    # dictstring = dict(zip(instring, outstring))
    # dictstring[" "] = " "
    # new_msg_list = []
    # for char in message:
    #     if char in instring:
    #         new_msg_list.append(dictstring[char])
    #     else:
    #         new_msg_list.append(char)
    # return "".join(new_msg_list)
    # return "".join(char if char not in instring else dictstring[char] for char in message)  # noqa
    return message.translate(str.maketrans(instring, outstring))


print(rot13("EBG13 rknzcyr"))
print(rot13("This is my first ROT13 excercise!"))
