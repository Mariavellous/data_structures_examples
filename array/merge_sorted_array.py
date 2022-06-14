"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing
order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate
this, nums1 has length of m + n, where the first m elements denote the elements that should be merged, and the lat n
elements are set to 0 and should be ignored nums2 has a length of n.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums1):
            while j < len(nums2):
                if nums1[i] == nums2[j]:
                    nums1.insert(i, nums2[j])
                    j += 1
                    i += 1
                elif nums1[i] < nums2[j] and nums1[-1] == nums1[i]:
                    nums1.append(nums2[j])
                    j += 1
                elif nums1[i] <= nums2[j] and nums1[i + 1] > nums2[j]:
                    nums1.insert(i + 1, nums2[j])
                    j += 1
                    i += 1
                i += 1
            i += 1
        return nums1




def main():
    my_solution = Solution().merge(nums1=[1, 2, 3], m=3, nums2=[2, 5, 6], n=3)

    print(my_solution)


if __name__ == "__main__":
      main()
