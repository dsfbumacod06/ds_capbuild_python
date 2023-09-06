'''
Write number in expanded form:
expanded_form(12) should return 10 + 2
expanded_form(42) should return 40 + 2
expanded_form(70304) should return 7000 + 300 + 4
'''


# my solution
def expanded_form2(num):
    num_len = len(str(num)) - 1
    addends = []
    while num_len > 0:
        if num % (factor := 10 ** num_len) != 0:
            addends.append(addend := (num // factor) * factor)
            num -= addend
            num_len -= 1
        else:
            num_len -= 1
    addends.append(num)
    return ' + '.join([str(x) for x in addends if x != 0])


# video solution
def expanded_form(num):
    num = list(str(num))
    # final = []
    # for y, x in enumerate(num):
    #     if x != '0':
    #         final.append(x + '0' * (len(num) - y - 1))
    # return final
    return ' + '.join(x + '0' * ((len(num)) - y - 1) for y, x in enumerate(num) if x != '0')  # noqa


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
print(expanded_form(904300))
print(expanded_form(9000000))
