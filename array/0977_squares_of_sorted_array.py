from typing import List
"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in 
non-decreasing order.
"""

# My Solution - Solution # 2 is better. Check it out.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        my_list = []
        for num in nums: #O(n)
            squared_num = num * num
            my_list.append(squared_num)
        my_list.sort() #O(n log n)
        return my_list

"""
Complexity Analysis
* Time Complexity: O(N log N), where N is the length of A.
* Space complexity : O(N) or O(logN)
    The space complexity of the sorting algorithm depends on the implementation of each program language.
    For instance, the list.sort() function in Python is implemented with the Timsort algorithm whose space complexity is O(N).
    In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is O(logN).
"""

# Solution # 2 - Better Time Complexity O(n) and Space Complexity O(n)
class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # make a list of 0's len(nums)
        result = [0] * n
        # left element / first element
        left = 0
        # right element / last element
        right = n - 1
        # Start at the last index to figure out the highest value element
        for i in range(n-1, -1, -1):
            # compare right vs left. Which is higher element?
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            # square the highest element and add it to the "i"th index
            result[i] = square * square
        return result


def main():
    # my_solution = Solution2().sortedSquares([-4, -1, 0, 3, 10])
    my_solution = Solution2().sortedSquares([-7, -3, 2, 3, 11])
    print(my_solution)




if __name__ == "__main__":
      main()