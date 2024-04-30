from typing import List

class Problem:
    # Merge the overlapping sub array in a given 2d array
    def question(self):
        arr = [[1, 3], [2, 4], [5, 7], [6, 8]]
        sol = Solution()
        arr = sol.merge_overlapping_intervals(arr)
        print(arr)
    

class Solution:
    def merge_overlapping_intervals(self, arr: List[List[int]])-> List[List[int]]:
        sorted(arr, key=lambda x: x[0])
        res = []
        for i in range(len(arr)):
            if (len(res) == 0) or (arr[i][0] > res[len(res) - 1][1]):
                res.append([arr[i][0], arr[i][1]])
            else:
                res[len(res) - 1][1] = max(res[len(res) - 1][1], arr[i][1])
        return res
    

if __name__ == "__main__":
    sol = Problem()
    sol.question()