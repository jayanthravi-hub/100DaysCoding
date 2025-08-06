def BubbleSort(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    print(f"{list1} is sorted order.")

list1 = list(map(int,input().split()))
print(list1)
BubbleSort(list1)
