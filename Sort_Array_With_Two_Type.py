# Given array has even and odd numbers :- sort array in such way that all odd come first and all even after that
from typing import List

class Problem:
    def question(self):
        arr = [15, 14, 13, 12]
        sol = Solution()
        # sol.solution_using_lomuto_algo(arr)
        sol.solution_using_hoare_algo(arr)
        print(arr)

class Solution:
    def solution_using_lomuto_algo(self, arr: List[int])-> None:
        i = -1
        j = 0
        while j < len(arr):
            if arr[j] % 2 != 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1

    def solution_using_hoare_algo(self, arr: List[int])-> None:
        i = -1
        j = len(arr)
        while True:
            while True:
                i += 1
                if arr[i] % 2 == 0:
                    break
            while True:
                j -= 1
                if arr[j] % 2 != 0:
                    break
            if i >= j:
                break
            arr[i], arr[j] = arr[j], arr[i]
        

if __name__ == "__main__":
    sol = Problem()
    sol.question()