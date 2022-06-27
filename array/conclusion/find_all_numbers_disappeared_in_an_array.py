"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the
range [1, n] that do not appear in nums.
"""

from typing import List

# TODO: Still need to find solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # TODO: try to do 2 passes approach next time and not nested loop
        disappeared_numbers = []
        for i in range(1, len(nums) + 1):
            if i not in nums:
                disappeared_numbers.append(i)
        return disappeared_numbers




def main():
    my_solution = Solution().findDisappearedNumbers(nums=[4, 3, 2, 7, 8, 2, 3, 1])
    # my_solution = Solution().findDisappearedNumbers(nums=[1, 1])
    print(my_solution)


if __name__ == "__main__":
    main()