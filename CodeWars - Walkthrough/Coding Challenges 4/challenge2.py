"""
Johnny is owrking as an intern for a publishing company, and was tasked with cleaning up old code.
He is working on a program that determins how many digits are all in the page numbers in a book 
with pages from 1 to n(inclusive).

For example, a book with 4 pages has 4 digits, 1 for each page.
While a 12-page book has 15 (9 for 1-9, plust 2 each for 10 11 12.)

Johnny;s boss, looking to future-proof, demanded that the new program be able to handle books up to
400,000,000,000,000,000 pages.
Example:

 - 6kyu Hardness
"""



# My Code
def page_digits(pages):
   num_strg = ""
#    pages = map(str,pages)
#    return pages
   for i in range(1,pages+1):
      num_strg += str(i)
   return len(num_strg)


def page_digits(pages):
   classifier = 0
   caser = 0
   multiplier1 = 1
   multiplier2 = '9876543210'
   while pages > classifier:
      caser += 1
      classifier += 9 * multiplier1
      multiplier1 *= 10
   return 9/10*int(multiplier2[-(caser):]) + (caser)*(pages -(classifier//10))


#Refactor




# Video Implementation / Alternate Implementations





# My Test
if __name__ == '__main__':
   print(page_digits(4)) # 4
   print(page_digits(12)) # 15
   print(page_digits(100)) # 192
   print(page_digits(9)) # 9
   print(page_digits(99)) # 189 -> 18 diff 2 * 9
   print(page_digits(90)) # 171
   print(page_digits(999)) # 2889
   print(page_digits(900)) # 2592 -> 297 diff 3 * 99
   print(page_digits(9999)) # 38889
   print(page_digits(9000)) # 34893 -> 3996 diff 4 * 999
   print(page_digits(9500)) # 36893
   print(page_digits(500)) # 1392 500 * 4
   print(page_digits(99999)) # 38889
   
