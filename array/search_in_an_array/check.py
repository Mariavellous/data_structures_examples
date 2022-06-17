"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M (i.e N = 2 * M)
More formally check if there exists two indices i and j such that: i =! j
"""

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for item in arr:
            n = item * 2
            if n != item and n in arr:
                return True
        return False


def main():
    # my_solution = Solution().checkIfExist(arr=[-2, 0, 10, -19, 4, 6, -8])
    # my_solution = Solution().checkIfExist(arr=[10, 2, 5, 3])
    # my_solution = Solution().checkIfExist(arr=[7, 1, 14, 11])
    # my_solution = Solution().checkIfExist(arr=[3, 1, 7, 11])
    # my_solution = Solution().checkIfExist(arr=[-10, 12, -20, -8, 15])
    my_solution = Solution().checkIfExist(arr=[0, 0])





    print(my_solution)

if __name__ == "__main__":
    main()