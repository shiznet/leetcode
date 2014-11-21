class Solution:
    # @return an integer
    def numTrees(self, n):
        array = []
        array.append(1)
        array.append(1)
        array.append(2)
        if n > -1 and n < 3:
            return array[n]
        for i in range(3,n+1):
            sum = 0
            for j in range(0,i):
                sum += (array[j] * array[i-1-j])
            array.append(sum)
        return array[-1] 
(array[j] * array[i-1-j])
if __name__ == "__main__":
    so = Solution()
    print so.numTrees(1)
