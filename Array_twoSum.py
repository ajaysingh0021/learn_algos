'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/546/

Two Sum
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1] 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i,j]

s = Solution()
# nums, target = [2,7,11,15], 9
# nums, target = [3,2,4],  6
nums, target = [3,3],  6
out = s.twoSum(nums, target)
print(f'{out=}')
print(f'Answer {nums[out[0]]} + {nums[out[1]]} = {target}')
