#-*- coding: cp937 -*-

class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
		"""
		只用O(k)space cost.那么就用一个list用来记录k列的记录
		"""
		
	
	def getKthRow(slef, upperRow,row):
		thisRow=[]
		if row<0:
			print 'wrong row number=%i' % row
		if row ==0 :
			return [1]
		for i in range(0,row):
			
