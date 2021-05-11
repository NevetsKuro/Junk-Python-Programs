#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def longestSubarray(arr):
    maxLen = 0
    for x in range(len(arr)):
        temp = []
        unique = []
        for y in range(x,len(arr)):
            temp.append(arr[y])
            if(arr[y] not in unique):
                unique.append(arr[y])
            if(len(unique)>2):
                break
            if(len(temp) and max(temp)-min(temp)<=1):
                if(maxLen<len(temp)):
                    maxLen = len(temp)
                    
    return maxLen

if __name__ == '__main__':
    print(longestSubarray([1,2,3,4,5]))