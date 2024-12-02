"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

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


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

from typing import List

# Brute Force O(n^2).
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i_1, value in enumerate(nums):
#             for i_2, sum_value in enumerate(nums[i_1:]):
#                 if value + sum_value == target:
#                     print([i_1, i_2])


# test = Solution()
# test.twoSum([2, 7, 11, 15], 9)

# Hash-table
class Solution_2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            print(numMap)
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found

test_2 = Solution_2()
print(test_2.twoSum([3,2,4], target=6))