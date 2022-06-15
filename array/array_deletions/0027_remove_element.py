"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of
the elements, may be changed. Since it's impossible to change the length of the array in some languages, you must instead
have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the
duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the
first k elements.
Return k after placing the final result in the first k slots of nums.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Solution 1 : Without changing the len(nums)
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        print(nums)
        return k

        # Solution 2: If you are able to change the len(nums) like in Python
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)


def main():
    my_solution = Solution().removeElement(nums=[3, 2, 2, 3], val=3)
    # my_solution = Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
    print(my_solution)

# Time Complexity: O(n)
# Space Complexity: O(1)


if __name__ == "__main__":
    main()