from typing import List

class Problem:
    # find the union of two sorted array
    def question(self):
        arr_1 = [3, 5, 8]
        arr_2 = [2, 8, 9, 10, 15]
        sol = Solution()
        res = sol.union_of_two_sorted_array(arr_1, arr_2)
        print(res)

class Solution:
    def union_of_two_sorted_array(self, arr_1: List[int], arr_2: List[int])-> List[int]:
        i = j = 0
        temp = []
        while i < len(arr_1) and j < len(arr_2):
            if i > 0 and arr_1[i] == arr_1[i - 1]:
                i += 1
                continue
            if j > 0 and arr_2[j] == arr_2[j - 1]:
                j += 1
                continue
            if arr_1[i] == arr_2[j]:
                temp.append(arr_1[i])
                i += 1
                j += 1
            elif arr_1[i] < arr_2[j]:
                temp.append(arr_1[i])
                i += 1
            else:
                temp.append(arr_2[j])
                j += 1
        while i < len(arr_1):
            temp.append(arr_1[i])
            i += 1
        while j < len(arr_2):
            temp.append(arr_2[j])
            j += 1
        return temp


if __name__ == "__main__":
    implementation = Problem()
    implementation.question()