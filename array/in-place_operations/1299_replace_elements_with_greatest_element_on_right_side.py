"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1
"""

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ## Neetcode Solution
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i]

        right_max = -1
        for i in range(len(arr) -1, -1, -1):
            new_max = max(right_max, arr[i])
            arr[i] = right_max
            right_max = new_max
        return arr
        # Time Complexity: O(n)

        ## My Solution works
        # # Loop from the last element first
        # # last element of the array
        # i = len(arr) - 1
        # # initial highest value is always the last element
        # highest = arr[i]
        # # loop through the element till the 0th index
        # while i > -1:
        #     # remember the current element
        #     current = arr[i]
        #     # special case: if this is the last index, replace the element with -1
        #     if i == len(arr) - 1:
        #         arr[i] = -1
        #     # replace the index with the highest value
        #     else:
        #         arr[i] = highest
        #
        #     # compare which is the highest value between the current and the previous highest value
        #     highest = max(current, highest)
        #     # iterate to the 0th index
        #     i -= 1
        # # return the list
        # return arr

        # Time Complexity: O(n)


        ## Trial 1: Time Limit Exceeded O(n^2)
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