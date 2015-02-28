class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if A is None or len(A)==0:
            return 0
        sum = 0
        max = A[0]
        if A is None:
            return 0
        for i in A:
            if sum<0:
                sum = i
            else:
                sum = sum+i
            if sum>max:
                max = sum
        return max
if __name__ == "__main__":
    so = Solution()
    import random
    array = range(-100,100)
    for i in range(10):
        sample = random.sample(array,10)
        print sample
        print so.maxSubArray(sample)
    
