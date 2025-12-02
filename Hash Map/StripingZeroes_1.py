class StripingZeroes:

    @staticmethod
    def stripingZeros(lst):
        if not lst or not lst[0]:
            return lst
        m,n = len(lst),len(lst[0])
        zero_row, zero_col = False, False
        for r in range(m):
            if lst[r][0] == 0:
                zero_col = True
                break
        for c in range(n):
            if lst[0][c] == 0:
                zero_row = True
                break
        for r in range(1,m):
            for c in range(1,n):
                if lst[r][c] == 0:
                    lst[r][0] = 0
                    lst[0][c] = 0
        for r in range(1,m):
            for c in range(1,n):
                if lst[r][0] == 0 or lst[0][c] == 0:
                    lst[r][c] = 0
        if zero_row:
            for c in range(n):
                lst[0][c] = 0
        if zero_col:
            for r in range(m):
                lst[r][0] = 0
        return lst



if __name__ == "__main__":     
    matrix = [
        [5, 1, 9, 11],
        [2, 0, 6, 8],
        [13, 3, 0, 7],
        [15, 14, 12, 16]
    ]
    result = StripingZeroes.stripingZeros(matrix)
    print(result)

'''
    time complexity: O(m*n) where m is number of rows and n is number of columns.
    space complexity: O(1) as we are using constant space.
'''