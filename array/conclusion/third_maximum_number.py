"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist,
return the maximum number.
"""

from typing import List

# TODO: Continue to work on the problem
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # start with the last element as the right_max
        right_max = nums[-1]
        for i in range(len(nums) - 1, -1, -1):
            # compare the right_max to value of the current ith index
            right_max = nums[i]
            new_max = max(right_max, nums[i - 1])
            nums[i] = new_max
            # right_max = nums[i - 1]
        return nums



def main():
    my_solution = Solution().thirdMax(nums=[3, 2, 1])
    my_solution = Solution().thirdMax(nums=[2, 2, 3, 1])
    print(my_solution)


if __name__ == "__main__":
    main()