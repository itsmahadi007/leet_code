from typing import List
from xmlrpc.client import MAXINT


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -MAXINT - 1
        max_ending_here = 0
        for i in range(0, len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    # max_so_far = -MAXINT - 1
    # max_ending_here = 0
    # for i in range(0, len(nums)):
    #     max_ending_here += nums[i]
    #     if max_so_far < max_ending_here:
    #         max_so_far = max_ending_here
    #     elif max_ending_here < 0:
    #         max_so_far = 0
    # return max_so_far


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    s = Solution()
    print(s.maxSubArray(nums))


main()
