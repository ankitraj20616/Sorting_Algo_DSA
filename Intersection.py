from typing import List
class Problem:
    # print the intersection of two sorted array :
    def question(self):
        arr_1 = [3, 5, 10, 10, 10, 15, 15, 20]
        arr_2 = [5, 10, 10, 15, 30]
        sol = Solution()
        res = sol.intersection(arr_1, arr_2)
        print(res)

class Solution:
    def intersection(self, arr_1: List[int], arr_2: List[int])-> List[int]:
        temp = []
        i = j = 0
        while i < len(arr_1) and j < len(arr_2):
            if i > 0 and arr_1[i] == arr_1[i - 1]:
                i += 1
                continue
            if arr_1[i] == arr_2[j]:
                temp.append(arr_1[i])
                i += 1
                j += 1
            elif arr_1[i] < arr_2[j]:
                i += 1
            else:
                j += 1
        return temp
                
if __name__ == "__main__":
    implementation = Problem()
    implementation.question()