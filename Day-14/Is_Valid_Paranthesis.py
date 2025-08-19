def is_valid(str1):
    stack = []
    dict1 = {')':'(', ']':'[', '}':'{'}

    for i in str1:
        if i in '[({':
            stack.append(i)
        else:
            if not stack or stack[-1] != dict1[i]:
                return False

            stack.pop()
    return len(stack) == 0

str1 = input()
print(is_valid(str1))
