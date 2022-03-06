class Solution:
    def fib(self, n: int) -> int:
        cache = [0] * (n + 1)
        print(cache)
        return fibn(n) * fibn(n)


def fibn(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibn(n - 1) + fibn(n - 2)


def main():
    salary = 4

    s = Solution()
    print(s.fib(salary))


main()
