'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

'''
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = list(set(nums))
        if len(nums) == len(x):
            return False
        else:
            return True

s = Solution()
nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
duplicateFound = s.containsDuplicate(nums)
print(f'{duplicateFound=}')
