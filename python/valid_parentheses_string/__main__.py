import unittest

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin,leftMax= 0,0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin,leftMax = leftMin -1,leftMax +1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin ==0
    

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().checkValidString("()"), True)

    def test_2(self):
        self.assertEqual(Solution().checkValidString("(*)"), True)

    def test_3(self):
        self.assertEqual(Solution().checkValidString("(*))"), True)

    def test_4(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_5(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_6(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_7(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_8(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_9(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_10(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_11(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_12(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_13(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_14(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_15(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_16(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_17(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_18(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_19(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_20(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_21(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_22(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

    def test_23(self):
        self.assertEqual(Solution().checkValidString("((*)"), True)

        

if __name__ == "__main__":

    unittest.main()