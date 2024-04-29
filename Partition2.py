from typing import List

class Problem:
    # Implementation of lomuto partition on array
    def question(self):
        arr = [10, 80, 30, 90, 40, 50, 70]
        sol = Solution()
        i = sol.lomutoPartition(arr, 0, len(arr) - 1)
        print(arr, i)

class Solution:
    def lomutoPartition(self, arr: List[int], low: int, high: int)-> int:
        i = low - 1
        j = low
        partition_element = arr[high]
        while j < high:
            if arr[j] < partition_element:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
        return i


if __name__ == "__main__":
    implementation = Problem()
    implementation.question()