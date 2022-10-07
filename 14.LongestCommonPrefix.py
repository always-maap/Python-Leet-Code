"""
14. Longest Common Prefix
Easy
String
---
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List


# O(S) time | O(1) space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, curr in enumerate(shortest):
            for other in strs:
                if other[i] != curr:
                    return shortest[:i]

        return shortest
