Problem Statement : Have the function OverlappingRanges(arr) take the array of numbers stored in arr which will contain 5 positive integers, the first two representing a range of numbers (a to b), the next 2 also representing another range of integers (c to d), and a final 5th element (x) which will also be a positive integer, and return the string true if both sets of ranges overlap by at least x numbers. For example: if arr is [4, 10, 2, 6, 3] then your program should return the string true. The first range of numbers are 4, 5, 6, 7, 8, 9, 10 and the second range of numbers are 2, 3, 4, 5, 6. The last element in the array is 3, and there are 3 numbers that overlap between both ranges: 4, 5, and 6. If both ranges do not overlap by at least x numbers, then your program should return the string false.

Code:

def OverlappingRanges(arr):
    var1 = arr[0]
    var2 = arr[1]
    var3 = arr[2]
    var4 = arr[3]
    var5 = arr[4]
    set1 = set(range(var1, var2+1))
    set2 = set(range(var3, var4+1))
    var6 = set1.intersection(set2)
    if len(var6) >= var5:
        return 'true'
    else:
        return 'false'

print(OverlappingRanges([1, 10, 9, 10, 1]))
