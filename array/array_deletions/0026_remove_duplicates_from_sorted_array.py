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
        # Solution # 1: Better Time Complexity but does not guarantee to return all the right elements in nums
        # This part handles edge case of len(nums <= 1
        if len(nums) <= 1:
            return len(nums)

        k = 0
        i = k + 1
        while i < len(nums):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
            i += 1
        return k + 1
        # Time Complexity: O(n)
        # Space Complexity: O(n)


        # Solution 2: If you are not supposed to change the len(nums) and keep all the original elements in nums
        # i = 0
        # j = i + 1
        # counter = 0
        # while i < len(nums) and nums[i] != "_":
        #     while j < len(nums):
        #         if nums[i] == nums[j]:
        #             nums[j] = "_"
        #             new = nums.pop(j)
        #             nums.append(new)
        #             counter += 1
        #         else:
        #             j += 1
        #     i += 1
        #     j = i + 1
        # return len(nums) - counter
        # Time Complexity : O(n * n)
        # Space Complexity: O(1)

        # Solution 3: If you can change the len(nums)
        # i = 0
        # j = i + 1
        # while i < len(nums):
        #     while j < len(nums):
        #         if nums[i] == nums[j]:
        #             nums.pop(j)
        #         else:
        #             j += 1
        #     i += 1
        #     j = i + 1
        # return len(nums)




def main():
    # my_solution = Solution().removeDuplicates(nums=[1, 1, 2])
    # my_solution = Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # my_solution = Solution().removeDuplicates(nums=[])
    my_solution = Solution().removeDuplicates(nums=[2])
    print(my_solution)


if __name__ == "__main__":
    main()