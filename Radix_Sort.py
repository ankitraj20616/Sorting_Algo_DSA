from typing import List

class Problem:
    def radix_sort(self):
        arr = [319, 212, 6, 8, 100, 50]
        sol = Solution()
        sol.radix_sort(arr)
        print(arr)

class Solution:
    def radix_sort(self, arr: List[int])-> None:
        max_element = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > max_element:
                max_element = arr[i]
        i = 1
        while (max_element//i) > 0:
            self.counting_sort(arr, i)
            i *= 10
    def counting_sort(self, arr: List[int], k: int)-> None:
        count = [0] * 10
        for i in range(len(arr)):
            count[(arr[i]//k) % 10] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        output = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            output[count[(arr[i]//k) % 10] - 1] = arr[i]
            count[(arr[i]//k) % 10] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]

if __name__ == "__main__":
    sol = Problem()
    sol.radix_sort()