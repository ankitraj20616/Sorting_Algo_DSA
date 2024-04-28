from typing import List

class Problem:
    # Count inversions in an array
    def question(self):
        arr = [2, 4, 1, 3, 5]
        sol = Solution()
        # res = sol.count_inversions_1(arr)
        res = sol.count_inversion_merge(arr, 0, len(arr) - 1)
        print(f"Numbers of inversions in an array is :- {res}")

class Solution:
    def count_inversions_1(self, arr: List[int])-> int:
        res = 0
        for i in range(len(arr) - 1):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    res += 1
        return res
    
    # Approach 2 using merge sort :-
    def count_inversion_merge(self, arr: List[int], low: int, high: int)-> int:
        res = 0
        if low < high:
            mid = low + ((high - low) // 2)
            res += self.count_inversion_merge(arr, low, mid)
            res += self.count_inversion_merge(arr, mid + 1, high)
            res += self.conqure(arr, low, mid, high)
        return res
    def conqure(self, arr: List[int], low: int, mid: int, high: int)-> int:
        left = [None] * (mid - low + 1)
        right = [None] * (high - mid)
        i = low
        j = mid + 1
        res = 0
        for x in range(len(left)):
            left[x] = arr[x + i]
        for x in range(len(right)):
            right[x] = arr[x + j]
        i, j = 0, 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
                k += 1
            else:
                res += len(left) - i
                arr[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return res
            

        
    
if __name__ == "__main__":
    implementation = Problem()
    implementation.question()