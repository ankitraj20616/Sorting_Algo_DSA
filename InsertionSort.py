from typing import List

class Problem_Insertion_Sort:
    def question(self):
        arr = [20, 5, 40, 60, 10, 30]
        sol = Solution()
        sol.insertion_sort(arr)
        print(arr)

class Solution:
    def insertion_sort(self, arr : List[int])->None:
        for i in range(1, len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                if arr[j] > temp:
                    arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
                


if __name__ == "__main__":
    implementation = Problem_Insertion_Sort()
    implementation.question()
