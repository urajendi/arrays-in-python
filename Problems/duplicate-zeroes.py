'''
	Problem: Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
    Note:
        The elements beyond the length of the original array are not written.
        1 <= arr.length <= 10000
        0 <= arr[i] <= 9
'''
from typing import List
    
def duplicateZeros(arr: List[int]) -> None:
    '''
        Time complexity: O(n)
        Space complexity: O(1)
    '''
    n = len(arr)
    i = 0
    while( i < n):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
            continue
        else:
            i += 1
    print("Array after adding duplicate zeroes:", arr)
        
def main ():
    '''
        n - Array size (int): 1 <= n <= 10000
        temp - Array elements (string of numbers in range [0,9])
    '''
    arr=[]
    print("Enter the array elements: ")
    temp=input()
    for i in temp.split():
        arr.append(int(i))
    n = len(arr)
    print("Array size = ", n)
    print("Array = ", arr)
    duplicateZeros(arr)
      
if __name__ == "__main__":
    main()