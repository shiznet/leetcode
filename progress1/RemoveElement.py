class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        index = 0
        length = len(A)
        tags=[]
        #tag
        for i in range(length):
            if elem == A[i]:
               tags.append(i)
        for i in tags[::-1]:
            A.pop(i)
        #remove
        return length - len(tags)

if __name__ == "__main__":
    so = Solution()
    list = [3,3]
    elem = 3
    print so.removeElement(list,elem)
