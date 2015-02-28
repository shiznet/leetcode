class Solution:
    # @return a list of integers
    def grayCode(self, n):
        result = [0]
        if n ==0 :
            return result
        rmnzp = 0
        cursor = 0
        while True:
            cursor = self.flipRightmostBit(cursor)
            result.append(cursor)
            rmnzp = self.rightMostNoneZeroPosition(cursor,n)
            if rmnzp == (n-1):
                break
            else:
                cursor = self.flip(cursor,rmnzp+1)
                result.append(cursor)
        return result

    def rightMostNoneZeroPosition(self,number,length):
        '''
        There must be another more elegant way to
        get right-most none-zero bit position
        '''
        counter = 0
        while (number & 0x1) == 0 and counter<=length:
            number = (number>>1)
            counter = counter+1
        return counter

    def flipRightmostBit(self,number):
        return self.flip(number,0)
    
    def flip(self,number,position):
        mask1 = 1<<position
        mask2 = ~mask1
        ori = (number & mask1)
        return (number&mask2) + (~ori & mask1)

if __name__ == "__main__":
    so = Solution()
    for i in range(6):
        print so.grayCode(i)
        print "\n"
