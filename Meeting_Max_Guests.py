from typing import List

class Problem:
    # Return the maximum number of guests we can meet :-
    # arr :- arrival timing of guests
    # dep :- departure timing of guests
    def question(self):
        arr = [900, 600, 700]
        dep = [1000, 800, 730]
        sol = Solution()
        res = sol.meeting_max_guests(arr, dep)
        print(res)

class Solution:
    def meeting_max_guests(self, arr: List[int], dep: List[int])-> int:
        arr = sorted(arr)
        dep = sorted(dep)
        i, j = 0, 0
        res, currnt = 0, 0
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                currnt += 1
                i += 1
            else:
                currnt -= 1
                j += 1
            res = max(res, currnt)

        return res
    
if __name__ == "__main__":
    sol = Problem()
    sol.question()