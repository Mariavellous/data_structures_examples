"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist,
return the maximum number.
"""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        pass


def main():
    my_solution = Solution().thirdMax(nums=[3, 2, 1])
    print(my_solution)


if __name__ == "__main__":
    main()