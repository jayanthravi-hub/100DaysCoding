def insertionSort(list1):
    for i in range(1, len(list1)):
        current_val = list1[i]
        pos = i
        while current_val < list1[pos-1] and pos > 0:
            list1[pos] = list1[pos-1]
            pos -= 1
        list1[pos] = current_val
    print(list1)
list1 = list(map(int,input().split()))
print(list1)
insertionSort(list1)
