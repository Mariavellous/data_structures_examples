"""
Given an array of integers arr, return true if and only if it is a valid mountain array.
"""

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # the len has to be more than 3 to create a mountain
        if len(arr) < 3:
            return False
        # highest point of the mountain
        peak = max(arr)
        # index of the peak
        index = arr.index(peak)

        # peak can't be the first or last element
        if peak == arr[0] or peak == arr[-1]:
            return False

        # going up the peak
        i = 0
        while i < index:
            if arr[i] < arr[i + 1]:
                i += 1
            else:
                return False

        # going down the peak
        while index < len(arr) - 1:
            if arr[index] > arr[index + 1]:
                index += 1
            else:
                return False

        # If we reach the end, the array creates a valid mountain.
        return True

    # Time Complexity: O(n)
    # Space Complexity: O(1)





def main():
    # my_solution = Solution().validMountainArray(arr=[0, 3, 2, 1])
    # my_solution = Solution().validMountainArray(arr=[3, 5, 5])
    my_solution = Solution().validMountainArray(arr=[2, 1])

    print(my_solution)


if __name__ == "__main__":
    main()