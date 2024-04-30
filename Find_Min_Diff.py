from typing import List
from MergeSort import Solution as mergeSort
from sys import maxsize
class Problem:
    # Return the minimum difference b/w any two elements in array
    def question(self):
        arr = [1, 8, 12, 5, 18]
        sol = Solution()
        res = sol.minimum_diff(arr)
        print(res)

class Solution:
    def minimum_diff(self, arr: List[int])-> int:
        sort = mergeSort()
        sort.merge_sort(arr, 0, len(arr) - 1)
        min_diff = maxsize
        for i in range(1, len(arr)):
            currnt_diff = arr[i] - arr[i - 1]
            if currnt_diff < min_diff:
                min_diff = currnt_diff
        return min_diff


if __name__ == "__main__":
    sol = Problem()
    sol.question()