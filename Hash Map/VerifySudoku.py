'''
Subgrids for a 9x9 Sudoku board can be represented as a 3x3 list of sets in Python. 
Each set will hold the numbers found in the corresponding subgrid.

[
  [set(), set(), set()],
  [set(), set(), set()],
  [set(), set(), set()]
]

'''

class verifySudoku:

    
    @staticmethod
    def VerifySudoku(board):
        rows= [set() for i in range(9)]
        cols= [set() for i in range(9)]
        subgrids=[[set() for i in range(3)] for i in range (3)]
        for r in range(9):
            for c in range(9):
                num =board[r][c]
                if num == 0:
                    continue
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in subgrids[r//3][c//3]:
                    return False
                rows[r].add(num)
                cols[c].add(num)
                subgrids[r//3][c//3].add(num)
        return True
if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 3, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    result = verifySudoku.VerifySudoku(board)
    print(result)

