Problem Statement : Have the function BitwiseOne(strArr) take the array of strings stored in strArr, which will only contain two strings of equal length that represent binary numbers, and return a final binary string that performed the bitwise OR operation on both strings. A bitwise OR operation places a 0 in the new string where there are zeroes in both binary strings, otherwise it places a 1 in that spot. For example: if strArr is ["1001", "0100"] then your program should return the string "1101"

Code :

def BitwiseOne(arr):
  var1 = arr[0]
  var2 = arr[1]
  str = ""
  for i in range(len(var1)):
      if var1[i] == '1' or var2[i] == '1':
          str += '1'
      else:
          str += '0'
  return str
  
print(BitwiseOne(['1001', '0100']))
