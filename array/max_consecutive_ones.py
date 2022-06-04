from typing import List
"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0
        for item in nums:
            if item == 1:
                current_length += 1

            else:
                if max_length < current_length:
                    max_length = current_length
                    current_length = 0

        if max_length < current_length:
            return current_length

        return max_length



def main():
    # my_solution = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    my_solution = Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
    print(my_solution)


if __name__ == "__main__":
      main()
