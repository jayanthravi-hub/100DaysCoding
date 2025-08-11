# leet code problem number 26

Reference:
# leetcode link:- https://leetcode.com/problems/remove-duplicates-from-sorted-array/ 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        for i in range(len(nums)):
            if nums[slow] != nums[i]:
                slow += 1
                nums[slow] = nums[i]
        print(nums[:slow+1])
        return slow + 1
    
        
