from typing import List


class Solution:
    def function1(self, x: int) -> int:
        for i in range(1, x):
            for j in range(x, i - 1, -1):
                print(j)

        return 0


def main():
    x = 10

    s = Solution()
    s.function1(x)


main()
