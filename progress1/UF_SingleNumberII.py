class Solution:
    # Negative
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        f = range(32)
        c = map(lambda x:0, f)
        mask = (1<<32) -1
        for i in A:
            counter = 0
            while (i & mask)==0x0 :
                bit = i & 0x1
                c[counter]=c[counter]+bit
                counter = counter+1
                i = (i>>1)
        result = map(lambda x:x%3,c)
        sum = 0
        for bit in range(32):
            sum = (sum<<1)+result[bit]
        return int(sum)
