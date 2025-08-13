def Container(list1):
    left = 0
    right = len(list1) - 1
    max_area = 0
    while left < right:
        base = right - left
        height = min(list1[left],list1[right])
        area = base * height
        max_area = max(area,max_area)

        if list1[left] < list1[right]:
            left += 1
        else:
            right -= 1

    return max_area

list1 = list(map(int,input().split()))
print(Container(list1))
