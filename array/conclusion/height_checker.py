"""
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in
non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the
expected height of the ith student in line.
You are given an integer array heights representing the current order that the students are standing in. Each heights[i]
is the height of the ith student in line (0-indexed).
Return the number of indices where heights[i] != expected[i]
"""

from typing import List

# TODO: Still need to work on this problem
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # this approach didn't work
        current_heights = heights
        heights.sort()
        print(heights)
        print(current_heights)




def main():
    my_solution = Solution().heightChecker(heights=[1, 1, 4, 2, 1, 3])
    print(my_solution)


if __name__ == "__main__":
    main()