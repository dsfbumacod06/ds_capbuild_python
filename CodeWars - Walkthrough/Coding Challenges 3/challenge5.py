""""
Pick Peaks
    - returns the positions, and the values "peaks" or the local maxima of a numeric array.
Example:
    arr = [ 0, 1, 2, 5, 1, 0] has a peack at position 3 with a value of 5. -> arr[3] = 5-> format is {pos: [], peaks: []}, empty arrays if no peaks.
    pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]) # returns {pos: [3,7], peaks: [6,3]}
    [1,2,2,2,1] has a peak - only return the position of the start of the plateau
    [1,2,2,2,2], [1,2,2,2,3] has no peak


 - 5kyu Hardness
"""



# My Code
# def pickPeaks(arr):
#     pos,peaks = [],[]
#     plat_pos,plat_value,flag = 0,0,0
#     for i in range(1,len(arr)-1):
#         if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
#             pos.append(i)
#             peaks.append(arr[i])
#         elif arr[i] > arr[i-1] and arr[i] == arr[i+1]:
#             plat_pos = i
#             plat_value = arr[i]
#             flag = 1
#         elif arr[i] == arr[i-1] and arr[i] > arr[i+1] and flag == 1:
#             pos.append(plat_pos)
#             peaks.append(plat_value)
#             flag = 0
#     return {f"'pos':{pos}, 'peaks':{peaks}"}


#Refactor
def pickPeaks(arr):
    pos = []
    flag = 0 # position when the current value overtook the previous value, if equal, equivalent to contnue
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            flag = i
        elif arr[i] < arr[i-1] and flag:
            pos.append(flag)
            flag = 0
    return {f"'pos':{pos}, 'peaks':{[arr[x] for x in pos]}"}



# Video Implementation / Alternate Implementations
# def pickPeaks():
#     return




# My Test
if __name__ == '__main__':
   print(pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3]))
   print(pickPeaks([1,2,2,2,1]))
   print(pickPeaks([3,2,3,6,4,1,2,3,2,2,2,2,1]))
   print(pickPeaks([3,2,3,6,4,1,2,3,1,2,2,2,1]))
   print(pickPeaks([1,2,2,2,2])) # no peak
   print(pickPeaks([1,2,2,2,3])) # no peak
