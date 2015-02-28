class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2 :
            return 2
        first = 1
        second = 2
        for i in range(2,n):
            tmp = second
            second = first + second
            first = tmp
        return second

if __name__ == "__main__":
    so = Solution()
    for i in range(1,20):
        print so.climbStairs(i)
