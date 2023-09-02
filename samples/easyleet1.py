# class Solution(object):
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         ref_sing = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }
#         ref_doub = {
#             "IV": 4,
#             "IX": 9,
#             "XL": 40,
#             "XC": 90,
#             "CD": 400,
#             "CM": 900
#         }
#         sum, i = 0, 0
#         while i < len(s):
#             if s[i: i + 2] in ref_doub.keys():
#                 sum += ref_doub[s[i: i + 2]]
#                 i += 2
#             else:
#                 sum += ref_sing[s[i]]
#                 i += 1
#         return sum

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")  # noqa
        return sum(map(lambda x: roman_to_integer[x], s))


s1 = Solution()
print(s1.romanToInt("III"))
print(s1.romanToInt("LVIII"))
print(s1.romanToInt("MCMXCIV"))
