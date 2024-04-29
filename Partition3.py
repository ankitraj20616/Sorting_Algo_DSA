from typing import List

class Problem:
    # Implementation of hoare's partition used in quick sort
    def question(self):
        arr = [5, 3, 8, 4, 2, 7, 1, 10]
        sol = Solution()
        j = sol.hoaresPartition(arr, 0, len(arr) - 1)
        print(arr, j)

class Solution:
    def hoaresPartition(self, arr: List[int], low: int, high: int)-> None:
        i = low - 1
        j = high + 1
        partition_element = arr[low]
        while True:
            while True:
                i += 1
                if arr[i] >= partition_element:
                    break
            while True:
                j -= 1
                if arr[j] < partition_element:
                    break
            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
        return i



if __name__ == "__main__":
    implementation = Problem()
    implementation.question()