class Solution:
    # @return an integer
    def totalNQueens(self, n):
        self.counter = 0
        self.n = n
        self.bsf(0, [])
        return self.counter

    def bsf(self, v, array):
        if v == self.n:
            self.counter += 1
            return
        else:
            for i in range(self.n):
                conflict = False
                for j in range(len(array)):
                    if (array[j] == i or
                                    v - j == array[j] - i or
                                    v - j == i - array[j]):
                        conflict = True
                        break
                if conflict:
                    continue
                na = array[::]
                na.append(i)
                self.bsf(v + 1, na)


if __name__ == "__main__":
    so = Solution()
    for i in range(1,10):
        print "%d %d" % (i,so.totalNQueens(i))

