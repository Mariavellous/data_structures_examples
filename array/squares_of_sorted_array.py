from typing import List
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in 
non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        my_list = []
        for num in nums:
            squared_num = num * num
            my_list.append(squared_num)
        my_list.sort()
        return my_list


def main():
    my_solution = Solution().sortedSquares([-4, -1, 0, 3, 10])
    # my_solution = Solution().findNumbers([555, 901, 482, 1771])
    print(my_solution)


if __name__ == "__main__":
      main()