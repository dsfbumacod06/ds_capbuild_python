""""
Weight for Weight
From normal sort, sort the weight by the sum of their digits.
Example:
    99 will have a "weight" of 18, 100 will have a "weight" of 1, so in the list, 100 will come before 99
 - 5kyu Hardness
"""



# My Code
# def order_weight(weights):
#     weight_dict = {}
#     for weight in weights.split():
#         final_Weight = 0
#         for num in weight:
#             final_Weight += int(num)
#         weight_dict[weight] = final_Weight   
#     return " ".join(sorted(sorted(weights.split()),key=lambda x: weight_dict[x]))



#Refactor
def order_weight(weights):
    return " ".join(sorted(sorted(weights.split()),key=lambda x: sum(int(c) for c in x)))

# Video Implementation / Alternate Implementations
# def order_weight(strng):
#     weights = strng.split()
#     order_weights = {}
#     for weight in weights:
#         sum = 0
#         for digit in weight:
#             sum += int(digit)
#         order_weights[weight] = sum
#     weights.sort()
#     weights.sort(key = lambda x: order_weights[x])
#     return " ".join(weights)


# My Test
if __name__ == '__main__':
    print(order_weight("56 65 74 100 99 58 86 180 90 900 9000"))