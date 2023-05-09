from typing import List
import unittest

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break

        return dp[0]

        

class Test(unittest.TestCase):

    def test_wordBreak(self):
        s = Solution()
        self.assertEqual(s.wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(s.wordBreak("applepenapple", ["apple", "pen"]), True)
        self.assertEqual(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
        self.assertEqual(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat", "an"]), True)
        self.assertEqual(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat", "an", "og"]), True)
    
if __name__ == '__main__':
    unittest.main()