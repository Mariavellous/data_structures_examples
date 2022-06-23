"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        pass


def main():
    my_solution = Solution().sortArrayByParity(nums = [0, 1, 0, 3, 12])
    print(my_solution)


if __name__ == "__main__":
    main()
