"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Better Solution
        right_pointer = 0
        left_pointer = 0
        while right_pointer in range(len(nums)):
            # if element is non-zero
            if nums[right_pointer] != 0:
                current_value = nums[left_pointer]
                # replace the left_pointer index to the element of the right_pointer index
                nums[left_pointer] = nums[right_pointer]
                # replace the right_pointer index to element 0
                nums[right_pointer] = current_value
                # increment the left_pointer index
                left_pointer += 1
            right_pointer += 1

            # Time Complexity: O(n)


        # # My Solution is Correct but there is a better code above.
        # # reverse iteration
        # for i in range(len(nums) - 1, -1, -1):
        #     # if the element in this index is equal to 0
        #     if nums[i] == 0:
        #         # remove the zero from that index
        #         nums.pop(i)
        #         # add the zero at the end of the array
        #         nums.append(0)
        #
        # # Time Complexity: O(n)


def main():
    my_solution = Solution().moveZeroes(nums = [0, 1, 0, 3, 12])
    # my_solution = Solution().moveZeroes(nums = [0])
    print(my_solution)



if __name__ == "__main__":
    main()
