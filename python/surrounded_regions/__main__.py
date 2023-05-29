from typing import List
import unittest
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])

        def capture(r,c):
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != "O":
                return 
            board[r][c] = "T"
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)

        # Capture the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if (board[r][c]=="O" and (r in [0,rows-1] or c in [0,cols-1])):
                    capture(r,c)
    


        # Capture surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Uncapture unsurrounded regions 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"



class Test(unittest.TestCase):
        
            def test_solve(self):
        
                s = Solution()
                board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","O","X"],
                        ["X","O","X","X"]]
                s.solve(board)
                self.assertEqual(board, [["X","X","X","X"],
                                        ["X","X","X","X"],
                                        ["X","X","X","X"],
                                        ["X","O","X","X"]])
                board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","O","X"],
                        ["X","O","O","X"]]
                s.solve(board)
                self.assertEqual(board, [["X","X","X","X"],
                                        ["X","O","O","X"],
                                        ["X","X","O","X"],
                                        ["X","O","O","X"]])
                board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","O","X"],
                        ["X","X","O","X"]]
                s.solve(board)
                self.assertEqual(board, [["X","X","X","X"],
                                        ["X","O","O","X"],
                                        ["X","X","O","X"],
                                        ["X","X","O","X"]])
                board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","O","X"],
                        ["X","O","O","X"]]
                s.solve(board)
                self.assertEqual(board, [["X","X","X","X"],
                                        ["X","O","O","X"],
                                        ["X","X","O","X"],
                                        ["X","O","O","X"]])
                board = [["X","X","X","X"],
                        ["X","O","O","X"],
                        ["X","X","X","X"],
                        ["X","O","O","X"]]
                s.solve(board)


if __name__ == '__main__':
    unittest.main()