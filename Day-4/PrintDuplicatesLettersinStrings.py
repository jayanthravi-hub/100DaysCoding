str1 = input()
x1 = {}
for i in range(len(str1)):
    if str1[i] in x1:
        x1[str1[i]] += 1
    else:
        x1[str1[i]] = 1
list1 = []
for key,value in x1.items():
    if value > 1 and key != " ":
        # print(key,end='')
        list1.append(key)
        # print(list(key),end=' ')
print(f"{list1} are the duplicate elements.")
