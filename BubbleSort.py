from typing import List
class Problem:
    def question(self):
        arr = [2, 10, 8, 7]
        # arr = [2, 3, 4, 5]
        sol = Solution()
        sol.bubble_sort(arr)
        print(arr)

class Solution:
    def bubble_sort(self, arr : List[int])->None:
        for i in range(len(arr) - 1):
            swap = False
            for j in range(1, len(arr) - i):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    swap = True
            if swap == False:
                return

if __name__ == "__main__":
    bubbleSort = Problem()
    bubbleSort.question()


