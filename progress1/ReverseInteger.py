class Solution:
    # @return an integer
    def reverse(self, x):
        minus = False
        reversed = 0
        if x < 0 :
            minus = True
            x = 0 - x
        while x > 0:
            last = x%10
            reversed = reversed*10 + last
            x = x /10
        if minus:
            reversed = 0 - reversed
        return reversed

if __name__ == "__main__" :
    so = Solution()
    print so.reverse(0)
    print so.reverse(123)
    print so.reverse(-123)
