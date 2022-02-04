from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1

            # If x is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1

            # means x is present at mid
            elif nums[mid] == target:
                return mid

        # If we reach here, then the element was not present
        return low


def main():
    nums = [1, 3, 5, 6]
    target = 5

    s = Solution()
    print(s.searchInsert(nums, target))


main()
