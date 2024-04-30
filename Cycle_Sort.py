from typing import List

class Problem:
    # Implementation of Cycle Sort Algo
    # Normal form or Cycle sort in which arr contain no. from 1 to len(arr)
    def question1(self):
        arr = [3, 5, 2, 1, 4]
        sol = Solution()
        sol.cycle_sort_1(arr)
        print(arr)
    
    # Complex implementation of cycle sort algo
    def question2(self):
        arr = [20, 40, 50, 10, 30]
        sol = Solution()
        sol.cycle_sort_2(arr)
        print(arr)

class Solution:
    def cycle_sort_1(self, arr: List[int])-> None:
        for i in range(len(arr)):
            correct_pos = arr[i] - 1
            if i != correct_pos:
                arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
            else:
                i += 1

    def cycle_sort_2(self, arr: List[int])-> None:
        for i in range(len(arr) - 1):
            pos = i
            item = arr[i]
            for j in range(i + 1, len(arr)):
                if arr[j] < item:
                    pos += 1
            if arr[pos] == item:
                continue
            arr[pos], item = item, arr[pos]
            while pos != i:
                pos = i
                for j in range(i + 1, len(arr)):
                    if arr[j] < item:
                        pos += 1
                if arr[pos] == item:
                    continue
                arr[pos], item = item, arr[pos]




if __name__ == "__main__":
    sol = Problem()
    sol.question2()