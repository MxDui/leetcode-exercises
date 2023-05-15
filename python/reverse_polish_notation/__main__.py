from typing import List
import unittest

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop() , stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        
        return stack[0]
    
class TestSolution(unittest.TestCase):
    def test_1(self):
        tokens = ["2","1","+","3","*"]
        self.assertEqual(Solution().evalRPN(tokens), 9)

    def test_2(self):
        tokens = ["4","13","5","/","+"]
        self.assertEqual(Solution().evalRPN(tokens), 6)

    def test_3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(Solution().evalRPN(tokens), 22)

if __name__ == "__main__":
    unittest.main()