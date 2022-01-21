from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # walk up
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False

        # walk down
        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N - 1


def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    s = Solution()
    print(s.validMountainArray(arr))


main()
