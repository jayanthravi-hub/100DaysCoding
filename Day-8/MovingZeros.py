# leetcode problem number 283

Reference:

# leetcode link :- https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = -1

        for i in range(0,len(nums)):
            if nums[i] != 0:
                slow += 1
                nums[slow],nums[i] = nums[i], nums[slow]
        print(nums)

        
