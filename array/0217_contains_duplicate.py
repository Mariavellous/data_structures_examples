from typing import List
"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.
"""

# Intuition: If there are any duplicate integers, they will be consecutive after sorting.
# Sorting is often a good preprocessing step.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # First, sort the list known to provide O (n log n)
        nums.sort()
        # The last element does not need to account for since it will be compared to the other elements from earlier
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False


def main():
    my_solution = Solution().containsDuplicate([1, 2, 3, 1])
    # my_solution = Solution().containsDuplicate([1, 2, 3, 4])
    # my_solution = Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(my_solution)


"""
Complexity Analysis

Time complexity: O(n log n). Sorting is O(n log n) and the sweeping is O(n). 
The entire algorithm is dominated by the sorting step, which is O(n log n).

Space complexity: O(1). Space depends on the sorting implementation which, usually, 
costs O(1) auxiliary space if heapsort is used.
"""

if __name__ == "__main__":
      main()


