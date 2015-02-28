class Solution:
    # @return an integer
    def romanToInt(self, s):
        """
        Input is guaranteed to be within the range from 1 to 3999.
        Priciples:
        1.I, II, III, IV, V, VI, VII, VIII, IX, X.
        2.I=1 V=5 X=10 L=50 C=100 D=500 M=1000
        3.I X C
        """
        if s == '' or len(s) ==0 :
            return 0
        if len(s) == 1:
            return self.romanLetterToInt(s[0])
        sum = 0
        first = self.romanLetterToInt(s[0])
        for i in range(1,len(s)):
            second = self.romanLetterToInt(s[i])
            if first < second:
                sum -= first
            else:
                sum += first
            first = second
        return sum+first

    def romanLetterToInt(self,c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        else:
            return 0

if __name__ == "__main__":
    so = Solution()
    roman='CCCXCIII'
    print so.romanToInt(roman)
