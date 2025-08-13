from pickletools import string1


def LongestSubstring(string1):
    left = 0
    right = 0
    s = set()
    max_length = 0
    while right < len(string1)-1:
        if string1[right] not in s:
            s = string1[right]
            right += 1
        else:
            s.remove([string1[left]])
            left += 1
        max_length = max(max_length, right-left)

    return max_length
string1 = input()
print(LongestSubstring(string1))



