from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) == 0:
            return False

        # arr[:] = [abs(ele) for ele in arr]
        arr[:] = sorted(arr, reverse=True)
        print(arr)
        length: int = len(arr)
        # for i in range(0, length):
        #     if arr[i] % 2 == 0 and arr[i] != 0:
        #         for j in reversed(arr):
        #             if arr[i] == j * 2:
        #                 return True
        #     else:
        #         continue
        # return False

        for i in range(0, length):
            if arr[i] % 2 == 0:
                for j in range(0, length):
                    if arr[i] == arr[j] * 2 and i != j:
                        return True
            else:
                continue
        return False


def main():
    arr = [0, 0]

    s = Solution()
    print(s.checkIfExist(arr))


main()
