from RomantoInteger import Solution as rso
class Solution:
    # @return a string
    def intToRoman(self, num):
        """
        Input is guaranteed to be within the range from 1 to 3999.        
        Priciples:
        1.I, II, III, IV, V, VI, VII, VIII, IX, X.
        2.I=1 V=5 X=10 L=50 C=100 D=500 M=1000
        3.I X C
        """
        #intToRmoanMap={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
        intToRomanMap={1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
        list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        if num <=0:
            return ""
        roman = "" 
        for k in list:
            times = num/k
            roman = roman+(intToRomanMap[k]*times)
            num = num-times*k
        return roman

if __name__ == "__main__":
    so = Solution()
    r = rso()
    for i in range(4000):
        converted = r.romanToInt(so.intToRoman(i))
        if converted == i:
            print False
            print i
