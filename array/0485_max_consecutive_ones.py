from typing import List
"""
Given a binary array nums (0's and 1's), return the maximum number of consecutive 1's in the array.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_length = 0
        for num in nums:
            if num == 1:
                current_length += 1
                # In the future, you can use max() function to compare which value is higher
                if max_length < current_length:
                    max_length = current_length
            else:
                current_length = 0

        return max_length

"""
Complexity Analysis
Time Complexity: O(N), where N is the number of elements in the array.
Space Complexity: O(1). We do not use any extra space.
"""

def main():
    # my_solution = Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    my_solution = Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
    print(my_solution)


if __name__ == "__main__":
      main()
