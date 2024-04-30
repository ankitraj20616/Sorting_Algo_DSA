from typing import List
class Problem:
    # Insert element in heap(max heap) and print heap
    def question_1(self):
        sol = Solution()
        sol.insertion(60)
        sol.insertion(20)
        sol.insertion(5)
        sol.insertion(100)
        sol.printHeap()
        sol.deletion()
        sol.printHeap()
    
    # Implementaion of heapify algo :- use to check tha heap is max heap or not/ heap is min heap or not
    def question_2(self):
        arr = [-1, 54, 53, 55, 52, 50]
        sol = Solution()
        for i in range((len(arr)-1)//2, 0, -1):
            sol.heapify(arr, len(arr) - 1, i)
        print(arr)

    def heap_sort(self):
        arr = [-1, 70, 60, 55, 45, 50]
        sol = Solution()
        sol.heap_sort(arr)
        print(arr)

class Solution:
    # Insertion in Heap
    def __init__(self) -> None:
        self.arr = [None] * 100
        self.size = 0
    def insertion(self, value):
        self.size += 1
        self.arr[self.size] = value
        i = self.size
        while i > 0:
            parent_node = i//2
            if parent_node > 0 and self.arr[parent_node] < self.arr[i]:
                self.arr[parent_node], self.arr[i] = self.arr[i], self.arr[parent_node]
                i = parent_node
            else:
                break
    
    # function to print heap
    def printHeap(self):
        print()
        for i in range(1, self.size + 1):
            print(self.arr[i], end=" ")

    # function to delete root node in heap
    def deletion(self):
        if self.size == 0:
            print("Noting to delete!")
            return
        self.arr[1] = self.arr[self.size]
        self.size -= 1
        i = 1
        while i <= self.size:
            left_child = i * 2
            right_child = i * 2 + 1
            if left_child <= self.size and self.arr[left_child] > self.arr[i]:
                self.arr[i], self.arr[left_child] = self.arr[left_child], self.arr[i]
                i = left_child
            elif right_child <= self.size and self.arr[right_child] > self.arr[i]:
                self.arr[i], self.arr[left_child] = self.arr[left_child], self.arr[i]
                i = left_child
            else: 
                break

    # function to check that any provided node is heap or not
    def heapify(self, arr: List[int], size: int, i: int)-> None:
        left_child = 2 * i
        right_child = 2 * i + 1
        largest = i
        if left_child <= size and arr[left_child] > arr[largest]:
            largest = left_child
        if right_child <= size and arr[right_child] > arr[largest]:
            largest = right_child
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, size, largest)
        else:
            return


    # Implementing heap sort
    def heap_sort(self, arr: List[int])-> None:
        # Converting heap into max heap
        for i in range((len(arr) - 1)//2, 0, -1):
            self.heapify(arr, len(arr) - 1, i)
        for i in range(len(arr) - 1, 1, -1):
            arr[i], arr[1] = arr[1], arr[i]
            self.heapify(arr, i - 1, 1)

if __name__ == "__main__":
    sol = Problem()
    # sol.question_1()  
    # sol.question_2()      
    sol.heap_sort()

