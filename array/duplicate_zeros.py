from typing import List
"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input 
array in place and do not return anything.
"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 1
            i += 1


def main():
    # my_solution = Solution().duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0])
    my_solution = Solution().duplicateZeros([1, 2, 3])
    print(my_solution)


if __name__ == "__main__":
      main()