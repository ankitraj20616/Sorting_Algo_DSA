from typing import List
import sys
class Problem:
    def question(self):
        arr = [10, 5, 20, 2, 18]
        sol = Solution()
        sol.selection_sort(arr)
        print(arr)

class Solution:
    def selection_sort(self, arr : List[int])->None:
        for i in range(len(arr)):
            currnt_min = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[currnt_min]:
                    currnt_min = j
            arr[i], arr[currnt_min] = arr[currnt_min], arr[i]


if __name__ == "__main__":
    implementaion = Problem()
    implementaion.question()
