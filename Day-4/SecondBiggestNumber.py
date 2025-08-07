def Second_Biggest(list1):
    if len(list1) < 2:
        print("the list should contains atleast 2 elements.")
        return
    first_max = float('-inf')
    sec_max = float('-inf')
    for i in range(len(list1)):
        if list1[i] > first_max:
            sec_max =   first_max
            first_max = list1[i]
        elif list1[i] > sec_max and list1[i] != first_max:
            sec_max = list1[i]
    if sec_max == float('-inf'):
        print("All the elements ar mostly equal.")
    else:
        print(f"{sec_max} is second biggest number in the list.")
list1 = list(map(int,input().split()))
Second_Biggest(list1)
