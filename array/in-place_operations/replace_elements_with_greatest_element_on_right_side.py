"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1
"""

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Trial 1: Time Limit Exceeded
        # i = 0
        # while i < len(arr):
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        #     else:
        #         highest_num = 0
        #         j = i + 1
        #         while j < len(arr):
        #             if arr[j] > highest_num:
        #                 highest_num = arr[j]
        #             j += 1
        #         arr[i] = highest_num
        #     i += 1
        # return arr


def main():
    # my_solution = Solution().replaceElements(arr=[17, 18, 5, 4, 6, 1])
    my_solution = Solution().replaceElements(arr=[400])
    print(my_solution)


if __name__ == "__main__":
    main()