from typing import List

class Problem:
    def counting_sort(self):
        arr = [1, 4, 4, 1, 0, 1]
        sol = Solution()
        sol.counting_sort_2(arr, 5)
        print(arr)

class Solution:
    def counting_sort_1(self, arr: List[int], k: int)-> None:
        count = [0] * k
        for i in range(len(arr)):
            count[arr[i]] += 1
        index = 0
        for i in range(len(count)):
            for j in range(count[i]):
                arr[index] = i
                index += 1
    def counting_sort_2(self, arr: List[int], k: int)-> None:
        count = [0] * k
        for i in range(len(arr)):
            count[arr[i]] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        output = [0] * len(arr)
        for i in range(len(arr)):
            output[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
    
if __name__ == "__main__":
    sol = Problem()
    sol.counting_sort()