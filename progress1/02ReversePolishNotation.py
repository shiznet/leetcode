#-*- coding: cp936 -*-
import sys

class Solution:
    def Div(self,i,j):
        flag=1
        if i<0:
            flag=flag*(-1)
        if j<0:
            flag=flag*(-1)
        if flag<0:
            return (i*(-1))/j*(-1)  
        else:
            return i/j

    def evalRPN(self, tokens):
        OP_PLUS = "+"
        OP_MINUS = "-"
        OP_MULTIPLE = "*"
        OP_DIVISION = "/"
        OPS = ["+", "-", "*", "/"]
        stack = []
        result = 0
        for element in tokens:
            """
            Check if is an operators.
            """
            if element in OPS:
                neg = stack.pop()
                passive = stack.pop()
                value = 0
                if OP_PLUS == element:
                    value = int(passive) + int(neg)
                elif OP_MINUS == element:
                    value = int(passive) - int(neg)
                elif OP_MULTIPLE == element:
                    value = int(passive) * int(neg)
                elif OP_DIVISION == element:
                    value = self.Div(int(passive),int(neg))
                stack.append(value)
            else:
                stack.append(element)
        result = stack.pop()
        return int(result)
        
so=Solution()
tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print so.evalRPN(tokens)
