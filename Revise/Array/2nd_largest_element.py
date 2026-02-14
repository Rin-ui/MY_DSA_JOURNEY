from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    first_largest = float('-inf')
    second_largest = float('-inf')
    
    for i in range(len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > first_largest:
            second_largest = first_largest
            first_largest = sequenceOfNumbers[i]
            
        elif sequenceOfNumbers[i] > second_largest and sequenceOfNumbers[i] < first_largest:
            second_largest = sequenceOfNumbers[i]
    
    if second_largest == float('-inf'):
        return -1
    else:
        return second_largest
# Taking input using fast I/O.
def takeInput():
    n = int(input())

    sequenceOfNumbers = list(map(int, input().strip().split(" ")))

    return sequenceOfNumbers, n

# Main.
t = int(input())
while t:
    sequenceOfNumbers, n = takeInput()
    print(findSecondLargest(sequenceOfNumbers))
    t = t-1
