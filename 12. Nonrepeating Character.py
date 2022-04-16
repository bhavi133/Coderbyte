Problem Statement : Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, and return the first non-repeating character. For example: if str is "agettkgaeee" then your program should return k. The string will always contain at least one character and there will always be at least one non-repeating character.

Code : 

def NonrepeatingCharacter(strParam):
  string = ""
  for i in strParam:
    if strParam.count(i) == 1:
      string += i
    else:
      pass
  return string[0]

# keep this function call here 
print(NonrepeatingCharacter(input()))
