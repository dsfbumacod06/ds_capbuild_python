""""
Once upon a time, on a way through the old wild mountainous west . . .
. . . a man was given direction to go from one point from another.
The directions were:
    "NORTH", "SOUTH', "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposites,
    "WEST" and "EAST" too.

Going to one direction and ocming back the opposite direction right away is a needless effort. 
Since this is the wild west, with dreatful weather and not much water, it's important to save
yourself some energy, otherwise you might die of thirst!
Example:
    How I crossed a mountain the smart way.
    The directions given to the man are for example:
        - ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    You can see that going NORTH and immediately going SOUTH is not reasonable, better stay to the same place!
    So the task is to give to the man a simplified version of the plan.A better plan in this case is simply:
        - ["WEST"]
 - 5kyu Hardness
"""


# My Code
# def dirReduc(arr):
#     y1 = arr.count("NORTH")
#     y2 = arr.count("SOUTH")
#     x1 = arr.count("EAST")
#     x2 = arr.count("WEST")
#     f_plan = []
#     y = y1 - y2
#     x = x1 - x2

#     if y > 0:
#         f_plan += ["NORTH"] * y
#     elif y < 0:
#         f_plan += ["SOUTH"] * abs(y)

#     if x > 0:
#         f_plan += ["EAST"] * x
#     elif x < 0:
#         f_plan += ["WEST"] * abs(x)
#     return f_plan

def dirReduc(arr):
    x, y = 0, 0
    dir_vals = {"NORTH":1, "SOUTH":-1, "WEST":-1, "EAST":1}
    for dir in arr:
        if dir in ["NORTH","SOUTH"]:
            y += dir_vals[dir]
        else:
            x += dir_vals[dir]
    f_plan = []
    f_plan += ["NORTH"] * y if y > 0 else ["SOUTH"] * abs(y)
    f_plan += ["EAST"] * x if x > 0 else ["WEST"] * abs(x)
    return f_plan




# Video Implementation / Alternate Implementations
# def dirReduc(arr):
#     change = False
#     for i in range(0, len(arr)):
#         if arr[i] 
#     return 0


    




# My Test
if __name__ == '__main__':
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])) # WEST
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST","EAST"])) # NONE
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH"])) # WEST SOUTH
    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "EAST", "NORTH"])) # NORTH
    print(dirReduc(["NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "EAST", "NORTH"])) # NORTH NORTH
