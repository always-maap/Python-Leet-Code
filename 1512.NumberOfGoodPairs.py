"""
1512. Number of Good Pairs
Easy
Array | Hash Table | Math | Counting
---
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0
"""

from typing import List


# O(2^n) time | O(1) space
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i, val in enumerate(nums):
            for val2 in range(i + 1, len(nums)):
                if val == nums[val2]:
                    count += 1
        return count
