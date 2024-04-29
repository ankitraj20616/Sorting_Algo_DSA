from typing import List
from QuickSort import Solution as quickSort
from sys import maxsize
class Problem:
    # Every element in array contain size of chocolate packet
    # m = no of children
    # Each child must get one packet only
    # Distribute in such a way that : max size packet - min size packet -> minimum
    def question(self):
        arr = [7, 3, 2, 4, 9, 12, 56]
        m = 3
        sol = Solution()
        res = sol.solution(arr, m)
        print(res)


class Solution:
    def solution(self, arr: List[int], m: int)-> int:
        sort = quickSort()
        sort.solution_using_lomuto(arr, 0, len(arr) - 1)
        res = maxsize
        for i in range(m - 1, len(arr)):
            currnt_diff = arr[i] - arr[i - (m - 1)]
            res = min(currnt_diff, res)
        return res


if __name__ == "__main__":
    res = Problem()
    res.question()