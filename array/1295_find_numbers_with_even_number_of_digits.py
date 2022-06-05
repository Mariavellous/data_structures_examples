from typing import List
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # initialize a counter for even-digit num
        num_of_even_digits = 0
        # take one element at a time
        for num in nums:
            # Convert num into string to find out the length of num
            num = str(num)
            # find out if length of num is even
            if len(num) % 2 == 0:
                # add to counter
                num_of_even_digits += 1

        return num_of_even_digits

def main():
    my_solution = Solution().findNumbers([12,345,2,6,7896])
    # my_solution = Solution().findNumbers([555, 901, 482, 1771])
    print(my_solution)

if __name__ == "__main__":
      main()