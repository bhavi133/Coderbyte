Problem Statement : Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.

import string

def CodelandUsernameValidation(strParam):
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    underscore = list('_')
    flag = 0
    str_list = list(strParam)
    if len(str_list) > 25 or len(str_list) < 4:
            flag = 0
    else:
        if strParam.startswith(tuple(letters)) and not strParam.endswith('_'):
            for i in strParam:
                if i in numbers or i in letters or i in underscore:
                    flag = 1

    if flag == 1:
        return 'true'
    else:
        return 'false'

keep this function call here 
print(CodelandUsernameValidation("u__hello_world123"))
