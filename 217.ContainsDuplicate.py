"""
217. Contains Duplicate
Easy
Array | Hash Table
---
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every
 element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List


# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for i in nums:
            if i in memo:
                return True
            else:
                memo[i] = i
        return False


# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
