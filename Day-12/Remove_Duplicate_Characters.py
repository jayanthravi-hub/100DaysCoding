"""Removing duplicate characters"""

def Remove_Duplicates(str1):
    result = ""
    seen = set()

    for i in range(len(str1)):
        if str1[i] not in seen:
            result += str1[i]
            seen.add(str1[i])
    return result

str1 = input()
print(Remove_Duplicates(str1))

"""Removing duplicate characters using two pointer technique"""

def remove_Duplicate(str1):
    n = len(str1)
    str1 = list(str1)
    if n == 0:
        return ""

    i = 0
    for j in range(1,n):
        duplicate = False
        for k in range(0,i+1):
            if str1[j] == str1[k]:
                duplicate = True
                break

        if not duplicate:
            i += 1
            str1[i] = str1[j]
    return "".join(str1[:i+1])

str1 = input()
print(remove_Duplicate(str1))
