"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
Return any array that satisfies this condition.
"""
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r = 0
        for i in range(len(nums)):
            # if element is even
            if nums[i] % 2 == 0:
                ### swap values of i index for r index
                # first, save the value of the current index
                current_value = nums[i]
                # change current index to value of r index
                nums[i] = nums[r]
                # change r index to current index value
                nums[r] = current_value
                # increment r
                r += 1
        return nums

    # Time Complexity = O(n)
    # Space Complexity = O(n)


def main():
    my_solution = Solution().sortArrayByParity(nums=[3, 1, 2, 4])
    # my_solution = Solution().sortArrayByParity(nums=[0])
    print(my_solution)


if __name__ == "__main__":
    main()
