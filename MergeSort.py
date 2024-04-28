from typing import List

class Problem:
    # question 1 :- merge two given sorted array 
    def question_1(self):
        arr_1 = [10, 15, 20]
        arr_2 = [5, 6, 6, 15]
        sol = Solution()
        res = sol.solution_1(arr_1, arr_2)
        print(res)

    # Given array has two part both are sorted merge it in such a way that whole array will sorted
    def question_2(self):
        arr = [10, 15, 20, 11, 30]
        sol = Solution()
        sol.solution_2(arr, 0, 2, len(arr))
        print(arr)

    # Merge Sort:
    def merge_sort_question(self):
        arr = [10, 5, 30, 15, 7]
        sol = Solution()
        sol.merge_sort(arr, 0, len(arr) - 1)
        print(arr)

class Solution:
    def solution_1(self, arr_1 : List[int], arr_2 : List[int])-> List[int]:
        i = j = 0
        res = [None] * (len(arr_1)+len(arr_2))
        index = 0
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] <= arr_2[j]:
                res[index] = arr_1[i]
                i += 1
                index += 1
            else:
                res[index] = arr_2[j]
                j += 1
                index += 1
        
        while i < len(arr_1):
            res[index] = arr_1[i]
            i += 1
            index += 1
        while j < len(arr_2):
            res[index] = arr_2[j]
            j += 1
            index += 1
        return res
    
    def solution_2(self, arr : List[int], low : int, mid : int, high : int)-> None:
        i = low
        j = mid + 1
        while i <= mid:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            i += 1

    def merge_sort(self, arr : List[int], low: int, high: int)-> None:
        if low < high:
            mid = low + ((high - low)//2)
            self.merge_sort(arr, low, mid)
            self.merge_sort(arr, mid + 1, high)
            self.conqure(arr, low, mid, high)
    
    def conqure(self, arr: List[int], low: int, mid: int, high: int)-> None:
        i = low
        j = mid + 1
        temp = [None] * (high - low + 1)
        index = 0
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp[index] = arr[i]
                i += 1
            else:
                temp[index] = arr[j]
                j += 1
            index += 1
        while i <= mid:
            temp[index] = arr[i]
            index += 1
            i += 1
        while j <= high:
            temp[index] = arr[j]
            index += 1
            j += 1
        for k in range(len(temp)):
            arr[low + k] = temp[k]

        


if __name__ == "__main__":
    implementation = Problem()
    # implementation.question_1()
    # implementation.question_2()
    implementation.merge_sort_question()