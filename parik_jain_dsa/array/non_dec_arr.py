from os import *
from sys import *
from collections import *
from math import *

def isPossible(arr, n):
    # Write your code here.
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            count+=1
            if count > 1:
                return False
        # decide which element to modify
            if i == 0 or arr[i-1] <= arr[i+1]:
                arr[i] = arr[i+1]
            elif arr[i-1] > arr[i+1]:
                arr[i+1] = arr[i]
    return True
