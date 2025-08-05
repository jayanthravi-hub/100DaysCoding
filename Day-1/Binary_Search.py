def binarySearch(list1, target):
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
    
list1 = list(map(int, input("Enter list elements (space-separated): ").split()))
target = int(input("Enter target element to search: "))

list1.sort()

index = binarySearch(list1, target)

if index != -1:
    print(f"Element found at index {index} (in sorted list)")
else:
    print("Element not found.")

