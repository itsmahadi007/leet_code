from typing import List


class Solution:
    def function1(self, a: int, r: int, p: int, n: int) -> int:
        result = a
        for i in range(1, n + 1):
            result += (a + (i * r)) ** p

        return result


def main():
    a = int(input("Enter an Integer a: "))
    r = int(input("Enter an Integer r: "))
    p = int(input("Enter an Integer p: "))
    n = int(input("Enter an Integer n: "))

    s = Solution()
    print(s.function1(a, r, p, n))


main()
