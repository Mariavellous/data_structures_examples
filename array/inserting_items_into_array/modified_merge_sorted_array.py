
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
    # my_solution = Solution().merge(nums1=[1, 2, 3], m=3, nums2=[2, 5, 6], n=3)
    # my_solution = Solution().merge(nums1=[1], m=1, nums2=[], n=0)
    # TODO: This is the edge case.
    my_solution = Solution().merge(nums1 = [], m = 0, nums2 = [1], n = 1)

    print(my_solution)


if __name__ == "__main__":
      main()
