Problem Statement : Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.

def FindIntersection(strArr):
    l = []
    for i in strArr:
        l.append(i.replace(","," ").lower().split())
    x1 = list(l[0])
    x2 = list(l[1])
    k = []
    for i in x1:
        if i in x2:
            k.append(i)

    if len(k) >= 1:
        return ','.join(k)
    else:
        return 'false'


print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))