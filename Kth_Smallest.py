from typing import List
from Partition2 import Solution as lomuto
class Problem:
    def question(self):
        arr = [10, 5, 30, 12]
        sol = Solution()
        res = sol.kth_smallest_element(arr, 3)
        print(res)

class Solution:
    def kth_smallest_element(self, arr: List[int], k: int)-> int:
        low = 0
        high = len(arr) - 1
        p = lomuto()
        while low <= high:
            i = p.lomutoPartition(arr, low, high)
            if i == k - 1:
                return arr[i]
            elif i < k - 1:
                low = i + 1
            else:
                high = i - 1
        return -1


if __name__ == "__main__":
    solution = Problem()
    solution.question()