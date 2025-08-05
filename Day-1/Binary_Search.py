def binarySearch(list1,target):
    low = 0
    high = len(list1) - 1

    while low <= high:
        mid = (low + high) // 2

        if list1[mid] == target:
            return mid
        elif list1[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
list1 = list(map(int,input().split()))
target = int(input())
index = binarySearch(list1,target)
if index != -1:
    print(f"element found at {index}")
else:
    print("element not found.")

