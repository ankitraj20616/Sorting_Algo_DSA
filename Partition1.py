from typing import List

class Problem:
    # Partition the given array according to the last element of the array
    def question(self):
        arr = [3, 8, 6, 12, 10, 7]
        sol = Solution()
        sol.partition(arr, len(arr) - 1)
        print(arr)

class Solution:
    def partition(self, arr: List[int], p: int)-> None:
        temp = [None] * len(arr)
        index = 0
        for num in arr:
            if num < arr[p]:
                temp[index] = num
                index += 1
        temp[index] = arr[p]
        index += 1
        for num in arr:
            if num > arr[p]:
                temp[index] = num
                index += 1
        index = 0
        for num in temp:
            arr[index] = num
            index += 1

if __name__ == "__main__":
    implementation = Problem()
    implementation.question()