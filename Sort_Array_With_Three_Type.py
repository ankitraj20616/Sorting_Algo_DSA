from typing import List

class Problem:
    # Given array and pivot = 2 sort array in such a way that :- array contain arr[i] < p then arr[i] = p then arr[i] > p 
    def question(self):
        arr = [2, 1, 2, 20, 10, 20, 1]
        sol = Solution()
        sol.sort_array_with_three_type(arr, 2)
        print(arr)
    

class Solution:
    def sort_array_with_three_type(self, arr: List[int], p: int)-> None:
        low = 0
        mid = 0
        high = len(arr) - 1
        while mid <= high:
            if arr[mid] < p :
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == p:
                mid += 1
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high -= 1
        

if __name__ == "__main__":
    sol = Problem()
    sol.question()