#-*- coding:utf-8 -*-
import random
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A) == 0:
             return 0
        position = (len(A)-1)/2
        left = 0
        right = len(A)-1
        while left <= right:
            if A[position] == target:
                return position
            if A[position] > target:
                if position == left:
                    return position
                right = position -1
                position = (left+position-1)/2
                continue
            if A[position] < target:
                if position == right:
                    return position+1
                left = position+1
                position = (position+1+right)/2
                continue
        if A[position] < target:
            return position+1
        return position

if __name__ == "__main__":
    so = Solution()
    A = [1,3,5,6]
    i = 0
    while i<10:
        B = random.sample(range(0,100),10)
        z = random.randrange(0,100,1)
        B.sort()
        print B
        print z
        print so.searchInsert(B,z)
        i+=1
