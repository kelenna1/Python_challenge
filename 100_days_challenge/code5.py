# **Bubble Sort Implementation** – Implement the Bubble Sort algorithm.

def bubble(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break



arr = [10,2,3,4,5,99,23,22,27,49]
print(f"Original array: {arr}")
bubble(arr)
print("Sorted array:", arr)