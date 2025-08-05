def LinearSearch(list1, target):
    for i in range(len(list1)):
        if list1[i] == target:
            return i
    return -1

list1 = list(map(int,input().split()))
target = int(input())
index =LinearSearch(list1,target)
if index != -1:
    print(f"element found at", index)
else:
    print(f"element not found.")





