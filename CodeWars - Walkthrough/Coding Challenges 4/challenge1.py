""""
Facebook like system
Example:
    [] -> No one likes this.
    ['Peter'] -> Peter likes this
    ['Jacob','Alex'] -> Jacob and Alex likes this
    ['Max','John','Mark'] -> Max, John and Mark likes this.
    ['Alex','Jacob','Mark','Max'] -> Alex, John and 2 others like this.
 - 6kyu Hardness
"""



# My Code
# from switchcase import switch
# def likes(names):
#    # with switch(0) as case:
#    #    if case(0):
#    #       return "No one likes this"
#    #    if case(1):
#    #       return f"{names[0]} likes this."
#    #    if case(2):
#    #       return f"{names[0]}, and {names[1]} likes this."
#    #    if case(3):
#    #       return f"{names[0]}, {names[1]}, and {names[2]} likes this."
#    #    if case.default:
#    #       return f"{names[0]}, {names[1]}, and {len(names)-2} others likes this."
#    if len(names) == 0:
#       return "No one likes this"
#    elif len(names) == 1:
#       return f"{names[0]} likes this."
#    elif len(names) == 2:
#       return f"{names[0]}, and {names[1]} likes this."
#    elif len(names) == 3:
#       return f"{names[0]}, {names[1]}, and {names[2]} likes this."
#    else:
#       return f"{names[0]}, {names[1]}, and {len(names)-2} others likes this."



#Refactor




# Video Implementation / Alternate Implementations
def likes(names):
   n = len(names)
   return {
      0: "No one likes this.",
      1: "{} likes this.",
      2: "{} and {} like this",
      3: "{}, {}, and {} like this",
      4: "{}, {}, and {others} others like this."
   }[min(n,4)].format(*names[:3],others=n-2)




# My Test
if __name__ == '__main__':
   print(likes([])) 
   print(likes(['Peter'])) 
   print(likes(['Jacob','Alex'])) 
   print(likes(['Max','John','Mark'])) 
   print(likes(['Alex','Jacob','Mark','Max'])) 
