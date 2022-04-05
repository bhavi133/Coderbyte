Problem Statement : Have the function GCF(arr) take the array of numbers stored in arr which will always contain only two positive integers, and return the greatest common factor of them. For example: if arr is [45, 12] then your program should return 3. There will always be two elements in the array and they will be positive integers.

Code :

def GCF(arr):
    var1 = arr[0]
    var2 = arr[1]
    factor1 = [i for i in range(1, var1+1) if var1 % i == 0]
    factor2 = [i for i in range(1, var2+1) if var2 % i == 0]
    factor3 = [i for i in factor1 if i in factor2]
    return max(factor3)

print(GCF([1, 4]))
