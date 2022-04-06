Problem Statement : Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.

Code :

def ArrayAdditionI(arr):
  arr = [i for i in arr if i >= 1]
  max_element = max(arr)
  min_element = min(arr)
  nums = [i for i in arr if i != max_element]
  print(nums)
  if max_element <= sum(nums):
    return "true"
  else:
    return "false"

# keep this function call here 
print(ArrayAdditionI([3, 5, -1, 8, 12]))
