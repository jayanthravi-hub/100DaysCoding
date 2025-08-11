# leet code problem number:- 125

Refernce:
leetcode link :- https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:

        # this is using slicing technique
        # cleaned = "".join(ch.lower() for ch in s if ch.isalnum())

        # return cleaned == cleaned[::-1]   


        # this is using two pointer technique:
        cleaned = ""
        for i in s:
            if i.isalnum():
                cleaned += i.lower()
            
        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            
            left += 1
            right -= 1
        return True

            

            

        
