from typing import List


class Solution:
    def function1(self, x: int) -> int:
        r = 1
        r += x

        if x > 4 and x < 10:
            r += 2 * x
        elif x <= 4:
            r += 3 * x
        else:
            r += 4 * x

        return r


def main():
    x = 10

    s = Solution()
    print(s.function1(x))


main()
