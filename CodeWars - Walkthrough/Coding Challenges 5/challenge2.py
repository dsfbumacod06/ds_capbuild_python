'''
Coins

A random place has a currency system that consists of 2 coins.
You are given the value of the coins, they can be identical, and will always be positive.  # noqa
Find the largest value that any whole number combination of the two cannot produce.  # noqa
return -1 if there are no such value or if it is an infinite number.

Examples:
coins(1,1) -> -1  -> you can produce any number with this combination.
coins(2,3) -> 1 -> cannot produce 1 but every other number above 1 is possible.
coins(2,2) -> -1 -> cannot produce odd numbers, hence infinite
'''

# misunderstood the problem
# return the largest number you CANNOT produce!! not the number of whole numbers  # noqa
# def coins(coin1, coin2):
#     if coin1 % 2 == 0 and coin2 % 2 == 0:
#         return -1
#     if coin1 == 1 or coin2 == 1:
#         return -1
#     if 2 in [coin1, coin2] and (coin1 % 2 == 1 or coin2 % 2 == 1):
#         high_coin = max(coin1, coin2)
#         return sum(1 for i in range(1, high_coin) if i % 2 == 1)
#     return -1


# questionable
from math import gcd


def coins(coin1, coin2):
    # return -1 if gcd(coin1, coin2) != 1 else (coin1 - 1) * (coin2 - 1) - 1
    return -1 if gcd(coin1, coin2) != 1 else coin1 * coin2 - coin1 - coin2


print(coins(1, 1))
print(coins(2, 3))
print(coins(2, 2))
print(coins(2, 6))
print(coins(2, 7))
print(coins(3, 4))  # 10?
print(coins(7, 15))
