from typing import List
"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique elements
appears only once. The relative order of the elements should be kept the same. 
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in
the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k 
elements of nums should hold the final result. It does not matter what you leave beyong the first k elements.
Return k after placing the final result in the first k slots of nums.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            for j in range(len(i + 1, nums) - 1):
                if nums[i] == nums[j]:
                    pass


def main():
    my_solution = Solution().removeDuplicates(nums=[1, 1, 2])
    print(my_solution)


if __name__ == "__main__":
    main()