import unittest

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = MinStack()

    def test_minStack(self):
        self.sol.push(-2)
        self.sol.push(0)
        self.sol.push(-3)
        self.assertEqual(self.sol.getMin(), -3)
        self.sol.pop()
        self.assertEqual(self.sol.top(), 0)
        self.assertEqual(self.sol.getMin(), -2)

if __name__ == "__main__":
    unittest.main()