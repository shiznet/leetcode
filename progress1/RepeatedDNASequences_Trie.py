#!/usr/local/bin/python
initlist = [None, None, None, None]
dnaelemap = ['A', 'C', 'G', 'T']


class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        result = []
        if s is None or len(s) <= 10:
            return result
        normallist = self.normalize(s)
        head = Trie()
        head.build(normallist, 0)
        for i in range(1, len(normallist) - 10):
            cnt = head.build(normallist, i)
            if cnt >= 10:
                result.append(self.denormalize(normallist[i:cnt + i]))
        return result

    def normalize(self, s):
        normallist = []
        for e in s:
            if e == 'A':
                normallist.append(0)
            elif e == 'C':
                normallist.append(1)
            elif e == 'G':
                normallist.append(2)
            elif e == 'T':
                normallist.append(3)
        return normallist

    def denormalize(self, s):
        return "".join(map(lambda x: dnaelemap[x], s))


class Trie:
    def __init__(self):
        # self.element = initlist
        self.element = [None, None, None, None]

    def build(self, s, start):
        pointer = self
        counter = 0
        repeated = True
        for i in range(start, len(s)):
            e = s[i]
            if pointer.element[e] is None:
                pointer.element[e] = Trie()
                repeated = False
            pointer = pointer.element[e]
            if repeated:
                counter += 1
        return counter


if __name__ == "__main__":
    s = Solution()
    import time

    list = "TGCTCCTGTCACAACTTCTTTACCAGCCTGTTTTTCTAGAGTCGGCTCAAAACCTGCCTTTATGCGCAGCTGTCCACGAGAATTTCATGTTATCGAGGACCGCGATATACCCAATCGCGCGCCCCAGAAAAAAGAGTCTTACCAGATGTATACGGTGACGACCCAGTGGGTAAGACCGCTCTGCTCAGCGACCCGTCCATACCCACAGTCAGCCATGTGTGACATATCAGCGTGCATTCTTGATCTGTATGGGTGCGCTGCCCCCGCACTTGATGGGGTATGTGATGACTCCGCTCGGTAAGCAAGACCCTGGGGGTTCGGACGTAGGGTATACCCGAACTTCACGTATGCGGACACCAACGCACGTGCCAATTTATCTAACGTATGTCTCCATGCCGCCCAGAAGGTTAAAGTGGACCGCCGTTCGTATACTGTTTCTGCAATTGTGTGCGGCAGCACCAGGTAGAGAGCATTCTATTTCGCTAGCTAGTAAATCTACTTCACCGAGTCTGGAAGCTCCAATCGCTGTTTACAAACTTTTTGCCCCTGCGTGGGTCAGGCCATGTCCCGTTCCCGAGGATTCTAGCACTGACCTAGCCCTATATCACGAGCCGGGTTTTCTTAAAATAGAGATCGGGACGTTAAGGTCTTATGAACGGCTTCAGCTATCTTCCGCTTACCAACTGAGCCGAACTATCTCCGGGTGTTACATGGATCCTAAAATGCTCTCCAATTTTGCCCCTGCATGGTATTTCTCTTGAGACTACTGGATCTACCTGGGTTGTGCATGTTTCGTGTCTCTTCCGACGTTCGACAATTGGGGGCGACGCTTTAAGTTCTACTACGGTGAGATGCACATCCCACGGACGCCCTTTTCCTTTGGCTCTTCCTACGTTCGCGAGCGGTCCTGTAGGACAGTTGCTTTATGCCAACTTTTACGAGGGTGGAATACAGTATCGCCATGACACTCTGAAAAAGGATGGAAGACCTGAGATTCACC"
    print time.time()
    print s.findRepeatedDnaSequences(list)
    print time.time()