from typing import List
import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i,curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i+1,curStr+c)

        if digits:
            backtrack(0,"")

        return res
    

class TestSolution(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    def test_2(self):
        self.assertEqual(Solution().letterCombinations(""), [])

    def test_3(self):
        self.assertEqual(Solution().letterCombinations("2"), ["a","b","c"])

    def test_4(self):
        self.assertEqual(Solution().letterCombinations("3"), ["d","e","f"])

    def test_5(self):
        self.assertEqual(Solution().letterCombinations("4"), ["g","h","i"])

    def test_6(self):
        self.assertEqual(Solution().letterCombinations("5"), ["j","k","l"])

    def test_7(self):
        self.assertEqual(Solution().letterCombinations("6"), ["m","n","o"])

    def test_9(self):
        self.assertEqual(Solution().letterCombinations("8"), ["t","u","v"])

    def test_10(self):
        self.assertEqual(Solution().letterCombinations("9"), ["w","x","y","z"])

    def test_11(self):
        self.assertEqual(Solution().letterCombinations("23"), ["ad","ae","af","bd","be","bf","cd","ce","cf"])

    def test_12(self):
        self.assertEqual(Solution().letterCombinations("234"), ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"])



if __name__ == "__main__":
    unittest.main()
                                                                 

                                                                 