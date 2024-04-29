# Must visit all partition implementatio first

from typing import List
from Partition2 import Solution as lomuto
from Partition3 import Solution as hoare
class QuickSort:
    # Quick Sort using Lomuto Partition:-
    def quick_sort1(self):
        arr = [8, 4, 7, 9, 3, 10, 5]
        sol = Solution()
        sol.solution_using_lomuto(arr, 0, len(arr) - 1)
        print(arr)

    # Quick Sort using Hoare's Partition:-
    def quick_sort2(self):
        arr = [8, 4, 7, 9, 3, 10, 5]
        sol = Solution()
        sol.solution_using_hoare(arr, 0, len(arr) - 1)
        print(arr)
        

class Solution:
    def solution_using_lomuto(self, arr: List[int], low: int, high: int)-> None:
        if low < high:
            p = lomuto()
            partition = p.lomutoPartition(arr, low, high)
            self.solution_using_lomuto(arr, low, partition - 1)
            self.solution_using_lomuto(arr, partition + 1, high)

    def solution_using_hoare(self, arr: List[int], low: int, high: int)-> None:
        if low < high:
            p = hoare()
            partition = p.hoaresPartition(arr, low, high)
            self.solution_using_lomuto(arr, low, partition)
            self.solution_using_lomuto(arr, partition + 1, high)


if __name__ == "__main__":
    implementation = QuickSort()
    implementation.quick_sort2()