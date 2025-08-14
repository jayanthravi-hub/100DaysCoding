def MergeSortedArray(nums1,nums2,m,n):
    nums1_copy = nums1[:m]
    i = 0
    j = 0
    k = 0
    while i < m and j < n:
        if nums1_copy[i] < nums2[j]:
            nums1[k] = nums1_copy[i]
            i += 1
            k += 1
        else:
            nums1[k] = nums2[j]
            j += 1
            k += 1
    while i < m:
        nums1[k] = nums1_copy[i]
        i += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1
    print(nums1)
list1 = list(map(int,input().split()))
list2 = list(map(int,input().split()))
m = int(input())
n = int(input())
MergeSortedArray(list1,list2,m,n)
