Problem Statement : Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"

import string

def LongestWord(sen):
    test_str = sen.translate(str.maketrans('', '', string.punctuation))
    l = [i for i in test_str.split()]
    return sorted(l, reverse=True, key=len)[0]

print(LongestWord("hello world"))
print(LongestWord("I love dogs"))
