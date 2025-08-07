# str1 = input()
# for i in range(len(str1)-1,-1,-1):
#     print(str1[i],end='')

# it is simple format
----------------------------------------------------------------

str1 = input()
word = ''
result=''

for i in str1:
    if i != ' ':
        word += i
    else:

        for j in range(len(word)-1,-1,-1):
            result += word[j]
        result += ' '
        word = ''

for i in range(len(word)-1,-1,-1):
    result += word[i]
print(result,end=' ')
