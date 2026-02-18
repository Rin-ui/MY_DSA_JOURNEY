from os import *
from sys import *
from collections import *
from math import *

from sys import stdin
import sys

def findSecondLargest(sequenceOfNumbers):
    # Write your code here.
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(len(sequenceOfNumbers)):
        if sequenceOfNumbers[i] > largest:
            second_largest = largest
            largest = sequenceOfNumbers[i]
        elif largest != sequenceOfNumbers[i] and sequenceOfNumbers[i] > second_largest:
            second_largest = sequenceOfNumbers[i]
    
        elif second_largest > sequenceOfNumbers[i]:
            continue
    if second_largest == float('-inf'):
                return -1

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
