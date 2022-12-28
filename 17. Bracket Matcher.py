Problem Statement : Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))", then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

def BracketMatcher(strParam):
  left_count = 0
  right_count = 0
  for i in strParam:
    if i == '(':
      left_count += 1
    elif i == ')':
      right_count += 1
    
    if right_count > left_count:
      return 0
    
  if left_count == right_count:
    return 1
  else:
    return 0

# keep this function call here 
print(BracketMatcher(raw_input()))
